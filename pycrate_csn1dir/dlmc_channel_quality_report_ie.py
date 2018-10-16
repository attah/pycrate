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
# * File Name : pycrate_csn1dir/dlmc_channel_quality_report_ie.py
# * Created : 2018-10-08
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.66 DLMC Channel Quality Report
# top-level object: DLMC Channel Quality Report IE



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

dlmc_bep_link_quality_measurements_struct = CSN1List(name='dlmc_bep_link_quality_measurements_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gmsk_mean_bep', bit=5),
    CSN1Bit(name='gmsk_cv_bep', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_8psk_mean_bep', bit=5),
    CSN1Bit(name='_8psk_cv_bep', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_16qam__nsr_mean_bep', bit=5),
    CSN1Bit(name='_16qam__nsr_cv_bep', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_32qam__nsr_mean_bep', bit=5),
    CSN1Bit(name='_32qam__nsr_cv_bep', bit=3)])})])

dlmc_bep_measurements_struct = CSN1List(name='dlmc_bep_measurements_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reported_modulation', bit=2),
    CSN1Bit(name='mean_bep_tn0', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reported_modulation', bit=2),
    CSN1Bit(name='mean_bep_tn1', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reported_modulation', bit=2),
    CSN1Bit(name='mean_bep_tn2', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reported_modulation', bit=2),
    CSN1Bit(name='mean_bep_tn3', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reported_modulation', bit=2),
    CSN1Bit(name='mean_bep_tn4', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reported_modulation', bit=2),
    CSN1Bit(name='mean_bep_tn5', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reported_modulation', bit=2),
    CSN1Bit(name='mean_bep_tn6', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reported_modulation', bit=2),
    CSN1Bit(name='mean_bep_tn7', bit=4)])})])

dlmc_interference_measurement_report_struct = CSN1List(name='dlmc_interference_measurement_report_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn0', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn1', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn2', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn3', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn4', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn5', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn6', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn7', bit=4)])})])

dlmc_channel_quality_report_ie = CSN1List(name='dlmc_channel_quality_report_ie', list=[
  CSN1Bit(name='c_value', bit=6),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='dlmc_interference_measurements', obj=dlmc_interference_measurement_report_struct)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='dlmc_bep_link_quality_measurements', obj=dlmc_bep_link_quality_measurements_struct),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='dlmc_bep_measurements', obj=dlmc_bep_measurements_struct)])})]),
  CSN1Val(name='', val='0')])
