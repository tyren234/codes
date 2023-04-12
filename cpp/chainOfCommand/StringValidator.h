#ifndef CHAINOFCOMMAND_STRINGVALIDATOR_H
#define CHAINOFCOMMAND_STRINGVALIDATOR_H

#include <string>

class StringValidator{
public:
    virtual ~StringValidator(){}
    virtual StringValidator* setNext(StringValidator* nextValidator) = 0;
    virtual std::string validate (std::string) = 0;
};

class BaseValidator : public StringValidator{
protected:
    StringValidator* next = nullptr;
public:
    virtual ~BaseValidator() { delete next; }
    StringValidator* setNext(StringValidator* nextValidator){
        next = nextValidator;
        return next;
    }
    std::string validate (std::string text){
        if (this->next){
            return this->next->validate(text);
        }
        return "Success!";
    }
};

#endif //CHAINOFCOMMAND_STRINGVALIDATOR_H
