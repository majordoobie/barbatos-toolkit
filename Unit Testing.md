---
parent file:
  - "[[Published]]"
related: 
creation data: 2023-12-05, 06:56
tags:
  - "#guides"
---

# Unit Testing
## Test-Driven Development (TDD) 
TDD is a software development process that relies on the repetition of very short development cycle to promote instant feedback loops. The feedback loop is often reffered to as the `tracer bullet development (TBD)` which is just a metaphor for software development based on the idea of instant, real-time feedback under actual conditions. It is based on the idea of taking some single feature, single action, single thread of work flow, and implementing it all the way through the system under construction. 

> The term "tracer bullet" comes from incendiary ammunition that gunners use to plot the trajectory of their shots

## Unit Testing vs Integration Testing vs Functional Testing
### Unit Testing
Unit testing is the process of testing that focuses on individual units or components of code. The goal of unit testing is to verify that each unit of code is working as expected in isolation. An example is creating some kind of command line parser that takes in different kinds of input and parses the input to present different *things*. For instance, a parameterized unit test could be used to test that when a user supplies a port number, that the number is within a specific range. This would all be unit tests testing that specific unit of the overall command line parser.

### Integration Testing
Integration testing is the process of testing that focuses on interactions between different units or components of code. Keeping with the same example, this would be completely parsing the command line tokens the user supplied and passing those arguments to the next portion of the code. 

### Functional Testing
Functional Testing is a type of testing that focuses on verifying that the software application meets the functional requirements specified in the requirements document. The goal of functional testing is to ensure that the software application is working as expected from the user's perspective.

## Unit Test Frameworks
The purpose of a unit test framework, like any other library, is to provide a standarized way to perform some kind of action and to avoid having to worry about creating your own test framework. Frameworks typically include some kind of test runner which is responsible for executing the tests and reporting the results along with including some kind of assertion library to perform the actual checks. 

In addition to providing the basics of assertion and reporting, frameworks will typically also provide a way to reduce code dup8ication by creating test fixtures. A fixture can be thought of as a struct containing the same information that all your unit tests need that fall under that said fixture. Keeping with the same example as above, say you are working on a series of tests that test your command line parser. You are focusing on some flag values that need to act on a file path that are all the same. You can create a test fixture which includes the file path so that you do not have to redefine that file path each time. In additional, you can even create the files in the fixture and then remove them when the fixture is done. More on that later. 


# GTest
## What is GTest
GTest ^[https://google.github.io/googletest/] is an open source unit testing framework for C++. It is popular because it is battle tested and easy to use. There is even CMake integrations with gtest along with IDEs such as CLion.

## GTest and C
It is quite common to use C++ to test C code, mainly because C++ is feature rich and makes it easy to quickly write unit tests with it. Since GTest is designed for testing C++ code, there is a couple limitations to using the framework for you C code. 

### C++ Mangle Functions
C++ supports the ability to overload a function name which is a feature that is not supported in C. So, when trying to call a C function within your C++ code you can find an error such as "cannot find function name". This is due to the function name mangling that C++ does. To get around this, you'll need to disable the mangling for the header file that you are including. This can be accomplished in two ways:

#### Extern
```c
#include <gtest/gtest.h>
extern "C" {
#include <some_c_header.h>
}
```

#### __cplusplus macro
```c
// File is some_c_header.h
#ifndef SOME_C_HEADER_H
#define SOME_C_HEADER_H

#ifdef __cplusplus
#extern "C" {
#endif // ENDS __cplusplus
}

#include <stdlib.h>
void my_func(char * val, int val2);

#ifdef __cplusplus
}
#endif // END __cplusplus

#endif SOME_C_HEADER_H_
```

## GTest and CMake
### Managing GTest Dependency
GTest is not a standard library, so it must be imported some how. The recommended way is through `git` which can just be added to the CMake of the project as a dependency.

```cmake
include (FetchContent)

IF (CMAKE_BUILD_TYPE STREQUAL "Debug")
```


---
# Resources