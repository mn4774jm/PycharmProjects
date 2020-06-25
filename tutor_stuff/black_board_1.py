'''This is a basic template for how mipo is generally set up. Keep in mind that if this code is placed into
an IDE like pycharm it will have errors, as it is not using descriptors rather than real variable names'''

def main():
    try:
        return_values_from_inputs = inputs()
        return_values_from_processing_block = processing(variables_you_need_to_use_in_processing)
        outputs(any_variables_you_want_to_send_to_outputs)
    except Exception as err:
        print(err)

def inputs():
    # write your code here
    return user_input_you_want_to_use_passed_to_main

def processing(parameters_that_you_passed_from_main):
    # write some code here
    return values_you_want_to_use_later_passed_to_main

def outputs(parameters_passed_from_main_block):
    # write your outputs here

main()