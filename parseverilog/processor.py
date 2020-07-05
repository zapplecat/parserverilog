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
    term_list = list(terms_map.values())
    for term in term_list:
        print(term.tostr())
        # rtype: str
        print(
            'Term Name: {}'.format(term.name))
        # rtype: set
        print(
            'Term Type: {}'.format(term.termtype))
        # rtype: int
        print(
            'Term msb {} and lsb {}'.format(term.msb, term.lsb))
        print('\n')

    # Getting Bind for each item
    print('\n\nBINDS')
    binds_map = analysis.getBinddict()
    for key, dataflow_bind in binds_map.items():
        print(dataflow_bind[0].tostr())
        # rtype: pyverilog.dataflow.dataflow.DFOperator
        print(
            'Bind Tree: {}'.format(dataflow_bind[0].tree))
        # rtype: str
        print(
            'Bind Tree Code: {}'.format(dataflow_bind[0].tree.tocode))
        print('\n')

    # top_ver.intsig Bind data
    intsig = list(binds_map.values())[2][0]
    table_demo(intsig, terms_map)


def table_demo(dest_bind, terms_map):
    print('\n\nDEMO TABLE')
    source_port_name = dest_bind.tree.name
    source_port = terms_map[source_port_name]
    source_port_io = 'i' if 'Output' in source_port.termtype else 'o'
    print('Source.Port,Destination.Port,Width,I/O')

    print(
        '{},{},[{}:{}],{}'.format(
            source_port_name,
            dest_bind.dest,
            source_port.msb,
            source_port.lsb,
            source_port_io)
    )
    print('\n\n')


if __name__ == '__main__':
    main()
