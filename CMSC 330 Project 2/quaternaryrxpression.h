// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the class definition of the QuaternaryExpression class, which is a subclass of Expression.
// Because it does not implement the abstract function evalauate, it is an abstract class. QuaternaryExpression
// objects are represented with the condition, case1, case2 and case3 expressions. The body of its constructor
// is defined in quaternaryexpression.cpp.

class QuaternaryExpression : public Expression {
public:
    QuaternaryExpression(Expression* condition, Expression* case1, Expression* case2, Expression* case3);
    double evaluate() override;
private:
    Expression* condition;
    Expression* case1;
    Expression* case2;
    Expression* case3;
};
