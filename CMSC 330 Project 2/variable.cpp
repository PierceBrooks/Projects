// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the body of the function contained in The Variable class. The evaluate function
// looks up te value of a variable in the symbol table and returns that value.

#include <iostream>
#include <fstream>
#include <sstream>

#include <string>
#include <vector>
using namespace std;

#include "expression.h"
#include "operand.h"
#include "variable.h"
#include "symboltable.h"
#include "expressionexception.h"

extern SymbolTable symbolTable;

Variable::Variable(string name){
    if (name.empty() || !isalpha(name[0])) {
        // Variable names must start with an alphabetic character
        throw ExpressionException("Variable names must start with an alpha numeric character or underscore");
    }

    this->name = name;
}

double Variable::evaluate() {
    return symbolTable.lookUp(name);
}
