from glob import glob
from pyverilog.dataflow.dataflow_analyzer import VerilogDataflowAnalyzer


RELATIVE_SAMPLE_INPUT_LOCATION = './sample_input/*.v'
TOP_MODULE_NAME = 'top_ver'


def main():
    # produces an arr of ['file1', 'file2', ...]
    sample_files = glob(RELATIVE_SAMPLE_INPUT_LOCATION)

    analysis = VerilogDataflowAnalyzer(
        sample_files,
        top_module=TOP_MODULE_NAME)  # Default is 'TOP'

    # Needed to generate analysis
    analysis.generate()

    # Getting Terms for each item

    # Getting Bind for each item


if __name__ == '__main__':
    main()
