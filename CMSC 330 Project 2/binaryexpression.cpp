// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the body of the functions contained in The BinaryExpression class, which includes
// the constructor that initializes the left and right expressions.
// Addition, subtraction, division, remainder, exponential, minimum, maximum and average are operators that are implemented.

#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
using namespace std;

#include "expression.h"
#include "expressionexception.h"
#include "binaryexpression.h"

BinaryExpression::BinaryExpression(Expression* leftOperand, char operation, Expression* rightOperand)
    : left(leftOperand), op(operation), right(rightOperand) {}

double BinaryExpression::evaluate()
{
    double leftValue= left->evaluate();
    double rightValue = right->evaluate();

    switch (op)
    {
        case '+':
            return leftValue + rightValue;
        case '-':
            return leftValue - rightValue;
        case '*':
            return leftValue * rightValue;
        case '/':
            if (rightValue == 0.0)
            {
                throw ExpressionException("Division by zero.");
            }

            return leftValue / rightValue;
        case '%':
            if (rightValue == 0.0)
            {
                throw ExpressionException("Modulus by zero.");
            }

            return fmod(leftValue, rightValue);
        case '^':
            return pow(leftValue, rightValue);
        case '<':
            return (leftValue < rightValue) ? leftValue : rightValue; // Minimum
        case '>':
            return (leftValue > rightValue) ? leftValue : rightValue; // Maximum
        case '&':
            return (leftValue + rightValue) / 2.0; // Average
        default:
            std::ostringstream error_message;
            error_message << "Unsupported binary operator: '" << op << "'";

            throw ExpressionException(error_message.str());
    }
}

