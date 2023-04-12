#include <iostream>
#include "UppercaseValidator.h"
#include "NumberValidator.h"
#include "LengthValidator.h"

int main() {
    std::string password;
    std::cout << "Insert password:" << std::endl;
    std::cin >> password;

    UppercaseValidator* uppercaseValidator = new UppercaseValidator();
    NumberValidator* numberValidator = new NumberValidator();
    int minimalPasswordLength = 8;
    LengthValidator* lengthValidator = new LengthValidator(minimalPasswordLength);

    uppercaseValidator->setNext(numberValidator)
                        ->setNext(lengthValidator);

    std::cout << uppercaseValidator->validate(password) << std::endl;

    return 0;
}
