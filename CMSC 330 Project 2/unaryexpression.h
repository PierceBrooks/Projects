// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the class definition of the UnaryExpression class, which is a subclass of Expression.
// Because it does not implement the abstract function evalauate, it is an abstract class. UnaryExpression
// objects are represented with an operand expression and an operator. The body of its constructor and the
// is defined in unaryexpression.cpp.

class UnaryExpression : public Expression {
public:
    UnaryExpression(Expression* operand, char op);
    double evaluate() override;
private:
    Expression* operand;
    char op;
};
