#ifndef CHAINOFCOMMAND_LENGTHVALIDATOR_H
#define CHAINOFCOMMAND_LENGTHVALIDATOR_H

#include "StringValidator.h"

class LengthValidator : public BaseValidator{
private:
    int minimalTextLength;
public:
    LengthValidator(int minimalTextLength){
        this->minimalTextLength = minimalTextLength;
    }

    std::string validate(std::string text) override{
        if (text.size() <= minimalTextLength){
            return "Validation unsuccessful: password has got too few letters";
        }
        else if (next){
            return next->validate(text);
        }
        return "Validation successful";
    }
};
#endif //CHAINOFCOMMAND_LENGTHVALIDATOR_H
