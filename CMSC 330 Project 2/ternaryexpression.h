// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the class definition of the TernaryExpression class, which is a subclass of Expression.
// Because it does not implement the abstract function evalauate, it is an abstract class. TernaryExpression
// objects are represented with a condition, true and false expressions. The body of its constructor
// is defined in ternaryexpression.cpp.

class TernaryExpression : public Expression {
public:
    TernaryExpression(Expression* condition, Expression* trueExpr, Expression* falseExpr);
    double evaluate() override;
private:
    Expression* condition;
    Expression* trueExpr;
    Expression* falseExpr;
};
