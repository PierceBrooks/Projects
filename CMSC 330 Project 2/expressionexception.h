// Pierce Brooks
// CMSC 330 Advanced Programming Languages
// Project 2 Skeleton
// UMGC CITE
// Fall 2023

// This file contains the class definition of the ExpressionException class, which is a subclass of std::runtime_error.
// It represents a custom exception

#include <stdexcept>
#include <string>

class ExpressionException : public std::runtime_error {
public:
    ExpressionException(const std::string& message) : std::runtime_error(message) {}
};
