#!/usr/bin/env python
# coding: utf-8

from utils import *
from logic import *

# from notebook import psource

(AKnight, AKnave, BKnight, BKnave, CKnight, CKnave) = symbols("AKnight, AKnave,BKnight, BKnave,CKnight, CKnave")

KBase1 = PropKB()
# KBase1 

# My Understanding of the puzzle - If A was a Knight they always tell the truth so they would just say they are a Knight
# because that's what they are, therefore it must be a knave because knaves lie

# Basic rules of puzzle

# A can either be a knight or (exclusively - xor) a knave
KBase1.tell('(AKnight ^ AKnave)')
# A can not be a knight and a knave
KBase1.tell('~(AKnight & AKnave)')

# 'I am both a Knight and a Knave'

# If A is a knight this implies that A is a knight and a knave (Knights tell the truth)
KBase1.tell(expr('AKnight ==> (AKnight & AKnave)'))

# If A is a Knave this implies that they are not both a Knight and a Knave
# ~ Not because knaves lie
KBase1.tell(expr('AKnave ==> ~(AKnight & AKnave)'))

KBase2 = PropKB()
# KBase2
# My understanding of the puzzle - Knights tell the truth so if A was a knight they would say they were a knight. And
# because knaves lie if both a and b were a knave they wouldn't say that both of them are knaves.
# Because B says nothing No implications can be made from B being a Knight and B being a Knave.

# Basic rules of puzzle

# A can either be a Knight or a Knave
KBase2.tell('(AKnight ^ AKnave)')
# B can either be a knight or a Knave
KBase2.tell('(BKnight ^ BKnave)')
# A can not be both a Knight and a Knave
KBase2.tell('~(AKnight & AKnave)')
# B can not be both a Knight and a Knave
KBase2.tell('~(BKnight & BKnave)')

# 'We are both knaves'

# If A is a Knight because knights tell the truth then this implies A and B are both Knaves
KBase2.tell(expr('AKnight ==> (AKnave & BKnave)'))
# If A is a Knave because knaves lie then this implies A and B are not both knaves
KBase2.tell(expr('AKnave ==> ~(AKnave & BKnave)'))

# 'B says nothing' no sentence needed for this

KBase3 = PropKB()
# KBase3
# Knights tell the Truth and Knaves lie
# My understanding of Puzzle - For A to be a Knight they would have to be telling the Truth so B would have to be a
# knight also, however B contradicts this by saying 'we are of different kinds'
# if B was also a Knight like A says they would have to be telling the truth therefore A is lying that B is a
# Knight therefore must be a Knave.

# Basic rules of puzzle

# A can either be a Knight or a Knave
KBase3.tell('(AKnight ^ AKnave)')
# B can either be a Knight or a Knave
KBase3.tell('(BKnight ^ BKnave)')
# A can not be both a Knight and a Knave
KBase3.tell('~(AKnight & AKnave)')
# B can not be both a Knight and a Knave
KBase3.tell('~(BKnight & BKnave)')

# We are of the same kind
# If A is a Knight then this implies A and B are both Knaves (the same kind) or
# A and B are both Knights (the same kind)
KBase3.tell(expr('AKnight ==> (AKnave & BKnave) ^ (AKnight & BKnight)'))
# If A is a Knave then this implies A and B are not both knaves (not the same kind) or A and B are not both Knights (
# not the same kind)
KBase3.tell(expr('AKnave ==> ~(AKnave & BKnave) & ~(AKnight & BKnight)'))

# 'We are of different Kinds' (We dont know who a or b is so we have to hypothesise if the statement was said by each
# character)
# If B is a Knight then this implies A is a Knave and B is a Knight (different kinds) or
# B is a Knave and A is a Knight (different kinds)
KBase3.tell(expr('BKnight ==> (AKnave & BKnight) ^ (BKnave & AKnight)'))
# If B is a Knave then this implies A is not a Knave and B is not a Knight (not different kinds) or B is not a Knave
# and A is not a Knight
KBase3.tell(expr('BKnave ==> ~(AKnave & BKnight) & ~(BKnave & AKnight)'))


KBase4 = PropKB()

# My Understanding of the puzzle - If A was a Knight they wouldn't be able to say I am a Knave as they would be lying
# and if A was a Knave they wouldn't be able to say I am a Knave as they would be telling the truth therefore
# A has to say 'I am a Knight'. Then B says A said I am a Knave which we know is a lie because no one can say that
# sentence so now we know B is a liar. B then says 'C is a Knave' because B is a liar this means C is actually a Knight
# and because C says A is a Knight A must be a Knight because Knights don't lie.

# Basic rules of puzzle

# A can either be a Knight or a Knave
KBase4.tell('(AKnight ^ AKnave)')
# B can either be a knight or a knave
KBase4.tell('(BKnight ^ BKnave)')
# C can either be a knight or a knave
KBase4.tell('(CKnight ^ CKnave)')
# A can not be both a Knight and a Knave
KBase4.tell('~(AKnight & AKnave)')
# B can not be both a knight and a knave
KBase4.tell('~(BKnight & BKnave)')
# C can not be both a knight and a knave
KBase4.tell('~(CKnight & CKnave)')

# A says either I am a Knight or I am a Knave but we do not know
# If A is a knight this implies that A is a Knight or a Knave
KBase4.tell(expr('AKnight ==> (AKnight ^ AKnave)'))
# If A is a knave this implies that A is not a knight or a Knave
KBase4.tell(expr('AKnave ==> ~(AKnight ^ AKnave)'))

# 'B says A said I am a knave'

# If B is a knave and A is a knave that implies A is a knave

# If B is a knave then they lied and A actually said 'I am a knight' and if A is a knave this statement is fine because
# knaves can say 'I am a knight' therefore if B and A are both Knaves then this implies that A can be a knave as
# opposed to if B was a Knight and A was a knave. B being a knight would be telling the truth and so A did say
# 'I am a knave' but knaves can't say that as it would be telling the truth therefore A could not be a knave.

KBase4.tell(expr('(BKnave & AKnave) ==> AKnave'))
# If B is a knave and A is a knight that implies A is not a knave
KBase4.tell(expr('(BKnave & AKnight) ==> ~AKnave'))
# If B is a knight and A is a knave that implies that A is not a knave
KBase4.tell(expr('(BKnight & AKnave) ==> ~AKnave'))
# If B is a knight and A is a knight that implies that A is a knave
KBase4.tell(expr('(BKnight & AKnight) ==> AKnave'))

# 'B then says C is a knave'

# If B is a knight this implies that C is a Knave
# If C is a Knave this implies B is a Knight because B said C is a knave. C being a Knave meant B told the truth and
# knights tell the truth.
KBase4.tell(expr('BKnight <=> CKnave'))
# If B is a knave this would imply that C is not a knave
# If C is not a Knave this implies that B is a knave because B said C is a knave. C not being a Knave meant B told a lie
# and Knaves tell lies
KBase4.tell(expr('BKnave <=> ~CKnave'))

# 'C says A is a knight'

# If c is a knight this implies A is a Knight
# Biconditional used here for same logic as above Biconditional
KBase4.tell(expr('CKnight <=> AKnight'))
# If c is a knave this implies A is not a knight
KBase4.tell(expr('CKnave <=> ~AKnight'))


# This function checks if any of the symbols are entailed by a given knowledge base, run this to file to check if
# your knowledge base has all sentences necessary to answer your query. No answer will be print if the knowledge base
# does not entail the query.
def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 1", KBase1),
        ("Puzzle 2", KBase2),
        ("Puzzle 3", KBase3),
        ("Puzzle 4", KBase4)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.clauses) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if knowledge.ask_if_true(symbol):  # model_check(knowledge, symbol):
                    print(f"    {symbol}")
    return


if __name__ == "__main__":
    main()
