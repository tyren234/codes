#ifndef CHAINOFCOMMAND_NUMBERVALIDATOR_H
#define CHAINOFCOMMAND_NUMBERVALIDATOR_H

#include "StringValidator.h"

class NumberValidator : public BaseValidator{
public:
    std::string validate(std::string text) override{
        bool hasNumber = false;
        for (char letter : text){
            if (isdigit(letter)){
                hasNumber = true;
                break;
            }
        }

        if (!hasNumber){
            return "Validation unsuccessful: password hasn't got any numbers";
        }
        else if (next){
            return next->validate(text);
        }
        return "Validation successful";
    }
};

#endif //CHAINOFCOMMAND_NUMBERVALIDATOR_H
