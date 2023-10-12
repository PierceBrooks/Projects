// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the class definition of the BinaryExpression class, which is a subclass of Expression.
// Because it does not implement the abstract function evalauate, it is an abstract class. BinaryExpression
// objects are represented with the left and right expressions and an operator character. The body of its constructor
// is defined in binaryexpression.cpp.

class BinaryExpression : public Expression {
public:
    BinaryExpression(Expression* left, char op, Expression* right);
    double evaluate() override;
private:
    Expression* left;
    char op;
    Expression* right;
};
