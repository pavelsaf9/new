def words_str(input_str):
    char_num = len(input_str)
    top_border = "+-" * char_num + "+\n"
    mid_str = "|" + "|".join(input_str) + "|\n"
    bottom_border = top_border
    output_str = top_border + mid_str + bottom_border

    return output_str
