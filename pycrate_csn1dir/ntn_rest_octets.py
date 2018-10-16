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
# * File Name : pycrate_csn1dir/ntn_rest_octets.py
# * Created : 2018-10-08
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.22c NT/N Rest Octets
# top-level object: NTN Rest Octets

# external references
from pycrate_csn1dir.notification_facch import group_call_information
from pycrate_csn1dir.notification_facch import emergency_ind

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

list_of_vstk_rand_information = CSN1List(name='list_of_vstk_rand_information', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='segment_id'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='vstk_rand', bit=36)])})]),
  CSN1Val(name='', val='0')])

list_of_reduced_gcr = CSN1List(name='list_of_reduced_gcr', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='reduced_gcr', bit=28)]),
  CSN1Val(name='', val='0')])

list_of_emergency_information = CSN1Alt(name='list_of_emergency_information', alt={
  '0': ('', []),
  '1': ('', [
  CSN1Ref(obj=emergency_ind),
  CSN1SelfRef()])})

list_of_group_call_nch_information = CSN1Alt(name='list_of_group_call_nch_information', alt={
  '0': ('', []),
  '1': ('', [
  CSN1Ref(obj=group_call_information),
  CSN1SelfRef()])})

ntn_rest_octets = CSN1List(name='ntn_rest_octets', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='nln_nch', bit=2)])}),
  CSN1Ref(obj=list_of_group_call_nch_information),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='cell_global_count', bit=2)])}),
    CSN1Ref(obj=list_of_reduced_gcr),
    CSN1Ref(obj=list_of_vstk_rand_information)]),
    'L': ('', []),
    None: ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(obj=list_of_emergency_information),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='priority_uplink_access')])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='fr_amr_config', bit=4)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='hr_amr_config', bit=4)])})])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='sms_data_confidentiality_ind'),
      CSN1Bit(name='sms_guaranteed_privacy_ind')])})]),
    'L': ('', []),
    None: ('', [])}),
  CSN1Ref(obj=spare_padding)])
