// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the body of the functions contained in The QuaternaryExpression class, which includes
// the constructor that initializes the condition, case1, case2 and case3 expressions.

#include <iostream>
#include <sstream>
using namespace std;

#include "expression.h"
#include "expressionexception.h"
#include "quaternaryrxpression.h"

QuaternaryExpression::QuaternaryExpression(Expression* conditionExpr, Expression* case1Expr, Expression* case2Expr, Expression* case3Expr)
    : condition(conditionExpr), case1(case1Expr), case2(case2Expr), case3(case3Expr){}

double QuaternaryExpression::evaluate(){
    double conditionValue = condition->evaluate();

    if (conditionValue < 0.0) {
        return case1->evaluate();
    } else if (conditionValue == 0.0) {
        return case2->evaluate();
    } else {
        return case3->evaluate();
    }
}
