#! /usr/bin/env python

#  $Id: po2ts.py 40 2007-08-06 11:18:04Z ogre.crewman $
#
#  This file is part of the UT3 project
#
#  Copyright (C) 2007 Marco Wegner <ogre.crewman@googlemail.com>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; see the file COPYING.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.


__version__ = "$Revision: 40 $"


# -----------------------------------------------------------------------------
# Import declarations
# -----------------------------------------------------------------------------

# modules
import sys
from ut3 import support
# classes
from optparse import OptionParser
from ut3.pofile import Ut3PoFile
from ut3.tsfile import Ut3TsFile
# functions
from optparse import make_option


# -----------------------------------------------------------------------------
# Global functions
# -----------------------------------------------------------------------------

def main( ):
    """
    The main function.

    @author: Marco Wegner
    """

    parser = OptionParser(usage="usage: %prog [options]", conflict_handler="resolve")
    parser.add_options(_get_local_options( ))

    (options, args) = parser.parse_args( )

    num_args = len(args)

    # there are arguments present - but we cannot do anything with them
    if num_args > 0:
        support.print_warning_message("unused argument(s) %s" % (" ".join(args)))

    # the script has been called without any options (but perhaps with
    # ususable arguments)
    if (len(sys.argv) - num_args) == 1:
        parser.print_help( )
        sys.exit( )

    # check if the input file is specified
    if options.infile is None:
        support.print_error_message("no input file specified")
        sys.exit( )
        
    pofile = Ut3PoFile(options.infile)
    tstore = pofile.parse( )

    tsfile = Ut3TsFile(options.outfile)
    tsfile.write(tstore)

    return


# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------

def _get_local_options( ):
    """
    Returns a list of options which are only used in this script.

    @return: The option list.
    """

    option_list = [
       make_option("-i", "--input", dest="infile", help="specify the input file"),
       make_option("-o", "--output", dest="outfile", help="specify the output file")
    ]

    return option_list

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main( )
