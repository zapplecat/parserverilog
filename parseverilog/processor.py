from glob import glob
from pyverilog.dataflow.dataflow_analyzer import VerilogDataflowAnalyzer


RELATIVE_SAMPLE_INPUT_LOCATION = './sample_input/*.v'
TOP_MODULE_NAME = 'top_ver'


def main():
    # produces an arr of ['file1', 'file2', ...]
    sample_files = glob(RELATIVE_SAMPLE_INPUT_LOCATION)

    analysis = VerilogDataflowAnalyzer(
        sample_files,
        topmodule=TOP_MODULE_NAME)  # Default is 'TOP'

    # Needed to generate analysis
    analysis.generate()

    # Getting Terms for each item
    print('\n\nTERMS')
    terms_map = analysis.getTerms()
    term_list = terms_map.values()
    for term in term_list:
        print(term.tostr())

    # Getting Bind for each item
    print('\n\nBINDS')
    binds_map = analysis.getBinddict()
    bind_list = binds_map.values()
    for bind in bind_list:
        print(bind[0].tostr())


if __name__ == '__main__':
    main()
