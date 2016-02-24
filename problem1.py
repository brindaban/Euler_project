def total_count(limit):
    count_for_three = (limit-1)/3;
    count_for_five = (limit-1)/5;
    count_for_fifteen = (limit-1)/15;
    total_count_for_multiply_of_three = (3*count_for_three*(count_for_three+1))/2
    total_count_for_multiply_of_five = (5*count_for_five*(count_for_five+1))/2
    total_count_for_multiply_of_fifteen = (15*count_for_fifteen*(count_for_fifteen+1))/2
    return total_count_for_multiply_of_three + total_count_for_multiply_of_five - total_count_for_multiply_of_fifteen


print total_count(1000)
