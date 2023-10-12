// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the body of the functions contained in The UnaryExpression class, which includes
// the constructor that initializes the operand expressions. Negation is the only operator that are implemented.

#include <iostream>
#include <sstream>
using namespace std;

#include "expression.h"
#include "expressionexception.h"
#include "unaryexpression.h"

UnaryExpression::UnaryExpression(Expression* operand, char operation)
    : operand(operand), op(operation){}

double UnaryExpression::evaluate(){
    double result= operand->evaluate();

    switch (op) {
        case '~':
            return -result;
            default:
                std::ostringstream error_message;
                error_message << "Unsupported unary operator: '" << op << "'";

                throw ExpressionException(error_message.str());
        }
}
