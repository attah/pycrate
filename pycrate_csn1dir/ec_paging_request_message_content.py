# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.3
# *
# * Copyright 2018. Benoit Michau. ANSSI.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/ec_paging_request_message_content.py
# * Created : 2018-10-08
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 9.1.63 EC PAGING REQUEST
# top-level object: EC Paging Request message content



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

ec_paging_request_message_content = CSN1List(name='ec_paging_request_message_content', list=[
  CSN1Bit(name='message_type', bit=4),
  CSN1Bit(name='used_dl_coverage_class', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='ec_page_extension', bit=4)])})])

mobile_identity_struct = CSN1Alt(name='mobile_identity_struct', alt={
  '0': ('', [
  CSN1Bit(name='p_tmsi', bit=32)]),
  '1': ('', [
  CSN1Bit(name='number_of_imsi_digits', bit=4),
  CSN1Bit(name='imsi_digits', bit=([1], lambda x: 4 * (x + 1)))])})
