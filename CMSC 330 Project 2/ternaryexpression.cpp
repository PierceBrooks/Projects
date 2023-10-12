// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the body of the functions contained in The TernaryExpression class, which includes
// the constructor that initializes the conditional, true and false expressions.
// Only the Conditional operator is implemented.

#include <iostream>
#include <sstream>
using namespace std;

#include "expression.h"
#include "expressionexception.h"
#include "ternaryexpression.h"

TernaryExpression::TernaryExpression(Expression* conditionExpression, Expression* trueExpression, Expression* falseExpression)
    : condition(conditionExpression), trueExpr(trueExpression), falseExpr(falseExpression){}

double TernaryExpression::evaluate(){
    double conditionValue = condition->evaluate();

    return (conditionValue != 0.0) ? trueExpr->evaluate() : falseExpr->evaluate();
}
