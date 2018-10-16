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
# * File Name : pycrate_csn1dir/single_downlink_assignment_2_ie.py
# * Created : 2018-10-08
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.48a.2 Single Downlink Assignment 2
# top-level object: Single Downlink Assignment 2 IE

# external references
from pycrate_csn1dir.egprs_level_ie import egprs_level_ie
from pycrate_csn1dir.egprs_window_size_ie import egprs_window_size_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

single_downlink_assignment_2_ie = CSN1List(name='single_downlink_assignment_2_ie', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='downlink_egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Bit(name='link_quality_measurement_mode', bit=2),
  CSN1Ref(name='downlink_egprs_level', obj=egprs_level_ie),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='event_based_fanr')])}),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='timeslot_allocation_c1', bit=8),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='timeslot_allocation_c2', bit=8)])})]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', [
      CSN1Alt(alt={
        '00': ('', []),
        '01': ('', []),
        '10': ('', [
        CSN1Bit(name='downlink_pdch_pairs_c1', bit=8),
        CSN1Bit(name='uplink_pdch_pairs_c1', bit=8)])}),
      CSN1Bit(name='rtti_downlink_pdch_pair_assignment_sc', bit=4)]),
      '1': ('', [
      CSN1Alt(alt={
        '00': ('', []),
        '01': ('', []),
        '10': ('', [
        CSN1Bit(name='downlink_pdch_pairs_c1', bit=8),
        CSN1Bit(name='downlink_pdch_pairs_c2', bit=8),
        CSN1Bit(name='uplink_pdch_pairs_c1', bit=8),
        CSN1Bit(name='uplink_pdch_pairs_c2', bit=8)])}),
      CSN1Bit(name='rtti_downlink_pdch_pair_assignment_dc', bit=8)])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='pfi', bit=7)])}),
  CSN1Bit(name='rlc_mode'),
  CSN1Bit(name='downlink_tfi_assignment', bit=5),
  CSN1Bit(name='control_ack'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='npm_transfer_time', bit=5)])})])
