#ifndef CHAINOFCOMMAND_UPPERCASEVALIDATOR_H
#define CHAINOFCOMMAND_UPPERCASEVALIDATOR_H

#include "StringValidator.h"

class UppercaseValidator : public BaseValidator{
public:
    std::string validate(std::string text) override{
        bool hasUpperLetter = false;
        for (char letter : text){
            if (isupper(letter)){
                hasUpperLetter = true;
                break;
            }
        }

        if (!hasUpperLetter){
            return "Validation unsuccessful: password hasn't got any uppercase letters";
        }
        else if (next){
            return next->validate(text);
        }
        return "Validation successful";
    }
};



#endif //CHAINOFCOMMAND_UPPERCASEVALIDATOR_H
