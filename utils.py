from xhtml2pdf import pisa


def convert_html_to_pdf(source_html_path, output_filename, context=None):
    """
    :param source_html_path: path of the html file
    :param output_filename: name of the output file
    :param context: dictionary of data which need to be passed as context
    :return: Boolen
    """
    # open output file for writing (truncated binary)
    source_html = open(source_html_path).read()
    if context:
        context_keys = []
        context_keys = map(context_keys.append(context), context)
        for context_key in context_keys:
            source_html = source_html.replace(context_key, context.get(context))
    result_file = open(output_filename, "w+b")
    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
        source_html,  # the HTML to convert
        dest=result_file)  # file handle to recieve result

    # close output file
    result_file.close()  # close output file

    # return False on success and True on errors
    return pisa_status
