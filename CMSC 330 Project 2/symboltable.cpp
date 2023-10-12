// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the body of the functions contained in The SymbolTable class. The insert function
// inserts a new variable symbol and its value into the symbol table and the lookUp function returns
// that value of the supplied variable symbol name.

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#include "symboltable.h"
#include "expressionexception.h"

void SymbolTable::insert(string variable, double value) {
    for (const Symbol& sym : elements) {
        if (sym.variable == variable) {
            std::ostringstream error_message;
            error_message << "Variable '" << variable << "' is initialized more than once in a statement.";

            throw ExpressionException(error_message.str());
        }
    }

    const Symbol& symbol = Symbol(variable, value);
    elements.push_back(symbol);
}

double SymbolTable::lookUp(string variable) const {

    for (int i = 0; i < elements.size(); i++)
        if (elements[i].variable == variable)
             return elements[i].value;

    std::ostringstream error_message;
    error_message << "Variable '" << variable << "' is uninitialized.";

    throw ExpressionException(error_message.str());
}

void SymbolTable::clear(){
    elements.clear();
}

