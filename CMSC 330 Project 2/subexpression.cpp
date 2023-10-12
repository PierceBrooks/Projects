// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the body of the functions contained in The SubExpression class, which includes
// the constructor that initializes the left and right subexpressions and the static function parse
// parses the subexpression.

#include <iostream>
#include <sstream>
using namespace std;

#include "expression.h"
#include "subexpression.h"
#include "operand.h"
#include "plus.h"
#include "minus.h"
#include "unaryexpression.h"
#include "binaryexpression.h"
#include "ternaryexpression.h"
#include "quaternaryrxpression.h"

SubExpression::SubExpression(Expression* left, Expression* right) {
    this->left = left;
    this->right = right;
}

Expression* SubExpression::parse(stringstream& in) {
    Expression * expression;
    Expression* left;
    Expression* right;
    char operation, paren;

    left = Operand::parse(in);
    in >> operation;

    if(operation == '~'){
         expression  =  new UnaryExpression(left,operation);
    }else if(operation == '?'){
        Expression* trueValue = Operand::parse(in);
        Expression* falseValue = Operand::parse(in);
        expression = new TernaryExpression(left,trueValue,falseValue);
    }else if(operation == '#'){
        Expression* case1 = Operand::parse(in);
        Expression* case2 = Operand::parse(in);
        Expression* case3 = Operand::parse(in);
        expression = new QuaternaryExpression(left,case1,case2,case3);
    }else{
        right = Operand::parse(in);

        expression =  new BinaryExpression(left,operation,right);
    }

    in >> paren;

    return expression;
}
