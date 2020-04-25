from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
def isTruth0(x):
    if (not (x[0] +x[1]==1)):
        return False
    return True

knowledge0 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),


    Implication(AKnight,And(AKnight,AKnave)),
    Implication(AKnave, Or(AKnave,AKnight)),
 
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    And(Or(CKnight,CKnave),Not(And(CKnight,CKnave))),

    Implication(AKnight,BKnight),
    Implication(AKnight,AKnave),
    Implication(AKnave, BKnight),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    And(Or(CKnight,CKnave),Not(And(CKnight,CKnave))),

    Implication(AKnight, BKnight),
    Implication(AKnave, BKnight),
    Implication(BKnight, AKnave),
    Implication(BKnave,AKnave),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    And(Or(CKnight,CKnave),Not(And(CKnight,CKnave))),

    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave),
    Implication(BKnight,CKnave),
    Implication(BKnave,CKnight),
    Implication(AKnave, BKnave),
   # Implication(AKnave, Implication(BKnight,AKnave)),
    Implication(BKnight,Or(Implication(AKnight,AKnave),Implication(AKnave,AKnight))),
    #if B tells truth, A was a knight who lied or a knave who told the truth
    Implication(BKnave,Or(Implication(AKnight,AKnight), Implication(AKnave, AKnave))),
    #if B is a knave then A was a knight who told the truth or  a knave who lied //always the case




)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
               # print("here")
                if model_check(knowledge, symbol):
                   # print("now")
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
