'''
This module was generated automatically. Do not edit directly.
'''

import collections
import ApiException
from   IpMgrConnectorMuxInternal import IpMgrConnectorMuxInternal

class IpMgrConnectorMux(IpMgrConnectorMuxInternal):
    '''
    \ingroup ApiConnector
    \brief Public class for IP manager connector, over SerialMux.
    '''

    #======================== commands ========================================

    ##
    # The named tuple returned by the dn_mux_hello() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>version</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_mux_hello = collections.namedtuple("Tuple_dn_mux_hello", ['RC', 'version'])

    ##
    # Sent by the manager to initiate a new session with a client.
    # 
    # \param version 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param secret 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_mux_hello named tuple.
    # 
    def dn_mux_hello(self, version, secret) :
        res = IpMgrConnectorMuxInternal.send(self, ['mux_hello'], {"version" : version, "secret" : secret})
        return IpMgrConnectorMux.Tuple_dn_mux_hello(**res)

    ##
    # 
    # 
    # \param version 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param cliSeqNo 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param mode 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: legacy
    # 
    # \returns The response to the command.
    # 
    def dn_hello(self, version, cliSeqNo, mode) :
        res = IpMgrConnectorMuxInternal.send(self, ['hello'], {"version" : version, "cliSeqNo" : cliSeqNo, "mode" : mode})
        return res

    ##
    # The named tuple returned by the dn_hello_response() function.
    # 
    # - <tt>successCode</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: success
    #      - 1: unsupported_version
    #      - 2: invalid_mode
    # - <tt>version</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>mgrSeqNo</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>cliSeqNo</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>mode</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: legacy
    # 
    Tuple_dn_hello_response = collections.namedtuple("Tuple_dn_hello_response", ['successCode', 'version', 'mgrSeqNo', 'cliSeqNo', 'mode'])

    ##
    # 
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_hello_response named tuple.
    # 
    def dn_hello_response(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['hello_response'], {})
        return IpMgrConnectorMux.Tuple_dn_hello_response(**res)

    ##
    # The named tuple returned by the dn_reset() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>macAddress</tt>: 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_reset = collections.namedtuple("Tuple_dn_reset", ['RC', 'macAddress'])

    ##
    # The reset command is used to reset various objects. The command argument is an object type, and if the object is a mote the MAC address must be specified (otherwise that argument is ignored).
    # 
    # \param type 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: resetSystem
    #      - 1: resetNetwork
    #      - 2: resetMote
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_reset named tuple.
    # 
    def dn_reset(self, type, macAddress) :
        res = IpMgrConnectorMuxInternal.send(self, ['reset'], {"type" : type, "macAddress" : macAddress})
        return IpMgrConnectorMux.Tuple_dn_reset(**res)

    ##
    # The named tuple returned by the dn_subscribe() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_subscribe = collections.namedtuple("Tuple_dn_subscribe", ['RC'])

    ##
    # 
    # 
    # The subscribe command indicates that the manager should send the external application the specified notifications. It contains two filter fields:
    # 
    # -filter is a bitmask of flags indicating the types of notifications that the client wants to receive
    # -unackFilter allows the client to select which of the notifications selected in filter should be sent acknowledged. If a notification is sent as 'acknowledged', thesubsequent notification packets will be queued while waiting for response.
    # 
    # Each subscription request overwrites the previous one. If an application is subscribed to data and then decides he also wants events he should send a subscribe command with both the data and event flags set. To clear all subscriptions, the client should send a subscribe command with the filter set to zero. When a session is initiated between the manager and a client, the subscription filter is initialized to zero.
    # 
    # The subscribe bitmap uses the values of the notification type enumeration. Some values are unused to provide backwards compatibility with earlier APIs.
    # 
    # \param filter 4-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # \param unackFilter 4-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_subscribe named tuple.
    # 
    def dn_subscribe(self, filter, unackFilter) :
        res = IpMgrConnectorMuxInternal.send(self, ['subscribe'], {"filter" : filter, "unackFilter" : unackFilter})
        return IpMgrConnectorMux.Tuple_dn_subscribe(**res)

    ##
    # The named tuple returned by the dn_getTime() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>uptime</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>utcSecs</tt>: 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>utcUsecs</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>asn</tt>: 5-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>asnOffset</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getTime = collections.namedtuple("Tuple_dn_getTime", ['RC', 'uptime', 'utcSecs', 'utcUsecs', 'asn', 'asnOffset'])

    ##
    # The getTime command returns the current manager UTC time and current absolute slot number (ASN). The time values returned by this command are delayed by queuing and transfer time over the serial connection. For additional precision, an external application should trigger the networkTime notification using the Time Pin. 
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getTime named tuple.
    # 
    def dn_getTime(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['getTime'], {})
        return IpMgrConnectorMux.Tuple_dn_getTime(**res)

    ##
    # The named tuple returned by the dn_setNetworkConfig() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_setNetworkConfig = collections.namedtuple("Tuple_dn_setNetworkConfig", ['RC'])

    ##
    # 
    # 
    # The setNetworkConfig command changes network configuration parameters. The response code indicates whether the changes were successfully applied. Generally, changes to network configuration will take effect when the manager reboots. Exceptions are detailed below:
    # 
    # 
    # -Max Motes: The new maxMotes value is used as soon as new motes try to join the network, but motes are not removed from the network if the value is set to a number lower than numMotes.
    # -Base Bandwidth: Changing baseBandwidth while the network is running does not reallocate bandwidth to Operational motes.
    # 
    # \param networkId 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param apTxPower 1-byte field formatted as a ints.<br/>
    #     There is no restriction on the value of this field.
    # \param frameProfile 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 1: Profile_01
    # \param maxMotes 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param baseBandwidth 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param downFrameMultVal 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param numParents 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param ccaMode 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: off
    #      - 1: energy
    #      - 2: carrier
    #      - 3: both
    # \param channelList 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param autoStartNetwork 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # \param locMode 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: off
    #      - 1: onDemand
    # \param bbMode 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: off
    #      - 1: upstream
    #      - 2: bidirectional
    # \param bbSize 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param isRadioTest 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param bwMult 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param oneChannel 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setNetworkConfig named tuple.
    # 
    def dn_setNetworkConfig(self, networkId, apTxPower, frameProfile, maxMotes, baseBandwidth, downFrameMultVal, numParents, ccaMode, channelList, autoStartNetwork, locMode, bbMode, bbSize, isRadioTest, bwMult, oneChannel) :
        res = IpMgrConnectorMuxInternal.send(self, ['setNetworkConfig'], {"networkId" : networkId, "apTxPower" : apTxPower, "frameProfile" : frameProfile, "maxMotes" : maxMotes, "baseBandwidth" : baseBandwidth, "downFrameMultVal" : downFrameMultVal, "numParents" : numParents, "ccaMode" : ccaMode, "channelList" : channelList, "autoStartNetwork" : autoStartNetwork, "locMode" : locMode, "bbMode" : bbMode, "bbSize" : bbSize, "isRadioTest" : isRadioTest, "bwMult" : bwMult, "oneChannel" : oneChannel})
        return IpMgrConnectorMux.Tuple_dn_setNetworkConfig(**res)

    ##
    # The named tuple returned by the dn_clearStatistics() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_clearStatistics = collections.namedtuple("Tuple_dn_clearStatistics", ['RC'])

    ##
    # The clearStatistics command clears the accumulated network statistics. The command does not clear path quality or mote statistics.
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_clearStatistics named tuple.
    # 
    def dn_clearStatistics(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['clearStatistics'], {})
        return IpMgrConnectorMux.Tuple_dn_clearStatistics(**res)

    ##
    # The named tuple returned by the dn_exchangeMoteJoinKey() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_exchangeMoteJoinKey = collections.namedtuple("Tuple_dn_exchangeMoteJoinKey", ['RC', 'callbackId'])

    ##
    # The exchangeMoteJoinKey command triggers the manager to send a new join key to the specified mote and update the manager's ACL entry for the mote. The response contains a callbackId. A commandFinished notification with this callbackId will be sent when the operation is complete. 
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # \param key 16-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_exchangeMoteJoinKey named tuple.
    # 
    def dn_exchangeMoteJoinKey(self, macAddress, key) :
        res = IpMgrConnectorMuxInternal.send(self, ['exchangeMoteJoinKey'], {"macAddress" : macAddress, "key" : key})
        return IpMgrConnectorMux.Tuple_dn_exchangeMoteJoinKey(**res)

    ##
    # The named tuple returned by the dn_exchangeNetworkId() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_exchangeNetworkId = collections.namedtuple("Tuple_dn_exchangeNetworkId", ['RC', 'callbackId'])

    ##
    # The exchangeNetworkId command triggers the manager to distribute a new network ID to all the motes in the network. AcallbackId is returned in the response. A commandFinished notification with this callbackId will be sent when the operation is complete.
    # 
    # \param id 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_exchangeNetworkId named tuple.
    # 
    def dn_exchangeNetworkId(self, id) :
        res = IpMgrConnectorMuxInternal.send(self, ['exchangeNetworkId'], {"id" : id})
        return IpMgrConnectorMux.Tuple_dn_exchangeNetworkId(**res)

    ##
    # The named tuple returned by the dn_radiotestTx() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_radiotestTx = collections.namedtuple("Tuple_dn_radiotestTx", ['RC'])

    ##
    # The radiotestTx command allows the user to initiate a radio transmission test. It may only be executed if the manager has been booted up in radiotest mode (see setNetworkConfig command). Three types of transmission tests are supported:
    # 
    # -Packet transmission
    # -Continuous modulation
    # -Continuous wave (unmodulated signal)
    # 
    # In a packet transmission test, the device generates a repeatCnt number of packet sequences. Each sequence consists of up to 10 packets with configurable size and delays. Each packet consists of payload of up to 125 bytes, and a 2-byte 802.15.4 CRC at the end. Bytes 0 and 1 contain the packet number (in big-endian format) that increments with every packet transmitted. Bytes 2..N contain a counter (from 0..N-2) that increments with every byte inside payload. Transmissions occur on the set of channels defined by chanMask, selected in pseudo-random order.
    # 
    # In a continuous modulation test, the device generates continuous pseudo-random modulated signal, centered at the specified channel. The test is stopped by resetting the device.
    # 
    # In a continuous wave test, the device generates an unmodulated tone, centered at the specified channel. The test tone is stopped by resetting the device.
    # 
    # 
    # 
    # Channel numbering is 0-14, corresponding to IEEE 2.4 GHz channels 11-25.
    # 
    # \param testType 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param chanMask 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param repeatCnt 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param txPower 1-byte field formatted as a ints.<br/>
    #     There is no restriction on the value of this field.
    # \param seqSize 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param pkLen_1 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param delay_1 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param pkLen_2 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param delay_2 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param pkLen_3 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param delay_3 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param pkLen_4 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param delay_4 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param pkLen_5 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param delay_5 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param pkLen_6 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param delay_6 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param pkLen_7 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param delay_7 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param pkLen_8 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param delay_8 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param pkLen_9 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param delay_9 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param pkLen_10 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param delay_10 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_radiotestTx named tuple.
    # 
    def dn_radiotestTx(self, testType, chanMask, repeatCnt, txPower, seqSize, pkLen_1, delay_1, pkLen_2, delay_2, pkLen_3, delay_3, pkLen_4, delay_4, pkLen_5, delay_5, pkLen_6, delay_6, pkLen_7, delay_7, pkLen_8, delay_8, pkLen_9, delay_9, pkLen_10, delay_10) :
        res = IpMgrConnectorMuxInternal.send(self, ['radiotestTx'], {"testType" : testType, "chanMask" : chanMask, "repeatCnt" : repeatCnt, "txPower" : txPower, "seqSize" : seqSize, "pkLen_1" : pkLen_1, "delay_1" : delay_1, "pkLen_2" : pkLen_2, "delay_2" : delay_2, "pkLen_3" : pkLen_3, "delay_3" : delay_3, "pkLen_4" : pkLen_4, "delay_4" : delay_4, "pkLen_5" : pkLen_5, "delay_5" : delay_5, "pkLen_6" : pkLen_6, "delay_6" : delay_6, "pkLen_7" : pkLen_7, "delay_7" : delay_7, "pkLen_8" : pkLen_8, "delay_8" : delay_8, "pkLen_9" : pkLen_9, "delay_9" : delay_9, "pkLen_10" : pkLen_10, "delay_10" : delay_10})
        return IpMgrConnectorMux.Tuple_dn_radiotestTx(**res)

    ##
    # The named tuple returned by the dn_radiotestRx() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_radiotestRx = collections.namedtuple("Tuple_dn_radiotestRx", ['RC'])

    ##
    # The radiotestRx command clears all previously collected statistics and initiates radio reception on the specified channel. It may only be executed if the manager has been booted up in radiotest mode (see setNetworkConfig command).During the test, the device keeps statistics about the number of packets received (with and without error).The test results may be retrieved using the getRadiotestStatistics command.
    # 
    # 
    # 
    # Channel numbering is 0-14, corresponding to IEEE 2.4 GHz channels 11-25.
    # 
    # \param mask 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param duration 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_radiotestRx named tuple.
    # 
    def dn_radiotestRx(self, mask, duration) :
        res = IpMgrConnectorMuxInternal.send(self, ['radiotestRx'], {"mask" : mask, "duration" : duration})
        return IpMgrConnectorMux.Tuple_dn_radiotestRx(**res)

    ##
    # The named tuple returned by the dn_getRadiotestStatistics() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>rxOk</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>rxFail</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getRadiotestStatistics = collections.namedtuple("Tuple_dn_getRadiotestStatistics", ['RC', 'rxOk', 'rxFail'])

    ##
    # This command retrieves statistics from a previously run radiotestRx command.It may only be executed if the manager has been booted up in radiotest mode (see setNetworkConfig command).
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getRadiotestStatistics named tuple.
    # 
    def dn_getRadiotestStatistics(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['getRadiotestStatistics'], {})
        return IpMgrConnectorMux.Tuple_dn_getRadiotestStatistics(**res)

    ##
    # The named tuple returned by the dn_setACLEntry() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_setACLEntry = collections.namedtuple("Tuple_dn_setACLEntry", ['RC'])

    ##
    # The setACLEntry command adds a new entry or updates an existing entry in the Access Control List (ACL).
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # \param joinKey 16-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setACLEntry named tuple.
    # 
    def dn_setACLEntry(self, macAddress, joinKey) :
        res = IpMgrConnectorMuxInternal.send(self, ['setACLEntry'], {"macAddress" : macAddress, "joinKey" : joinKey})
        return IpMgrConnectorMux.Tuple_dn_setACLEntry(**res)

    ##
    # The named tuple returned by the dn_getNextACLEntry() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>macAddress</tt>: 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>joinKey</tt>: 16-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getNextACLEntry = collections.namedtuple("Tuple_dn_getNextACLEntry", ['RC', 'macAddress', 'joinKey'])

    ##
    # 
    # 
    # The getNextACLEntry command returns information about next mote entry in the access control list (ACL). To begin a search (find the first mote in ACL), a zero MAC address (0000000000000000) should be sent.There is no mechanism for reading the ACL entry of a specific mote. This call is an iterator. If you call getNextACLEntry with mote A as the argument, your response is the ACL entry for mote B, where B is the next mote in the ACL.
    # 
    # 
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getNextACLEntry named tuple.
    # 
    def dn_getNextACLEntry(self, macAddress) :
        res = IpMgrConnectorMuxInternal.send(self, ['getNextACLEntry'], {"macAddress" : macAddress})
        return IpMgrConnectorMux.Tuple_dn_getNextACLEntry(**res)

    ##
    # The named tuple returned by the dn_deleteACLEntry() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_deleteACLEntry = collections.namedtuple("Tuple_dn_deleteACLEntry", ['RC'])

    ##
    # The deleteACLEntry command deletes the specified mote from the access control list (ACL). If the macAddress parameter is set to all 0xFFs or all 0x00s, the entire ACL is cleared.
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_deleteACLEntry named tuple.
    # 
    def dn_deleteACLEntry(self, macAddress) :
        res = IpMgrConnectorMuxInternal.send(self, ['deleteACLEntry'], {"macAddress" : macAddress})
        return IpMgrConnectorMux.Tuple_dn_deleteACLEntry(**res)

    ##
    # The named tuple returned by the dn_pingMote() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_pingMote = collections.namedtuple("Tuple_dn_pingMote", ['RC', 'callbackId'])

    ##
    # The pingMote command sends a ping (echo request) to the mote specified by MAC address. A unique callbackId is generated and returned with the response. When a ping response is received from the mote, the manager generates a ping notification with the measured round trip delay and several other parameters.
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_pingMote named tuple.
    # 
    def dn_pingMote(self, macAddress) :
        res = IpMgrConnectorMuxInternal.send(self, ['pingMote'], {"macAddress" : macAddress})
        return IpMgrConnectorMux.Tuple_dn_pingMote(**res)

    ##
    # The named tuple returned by the dn_getLog() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_getLog = collections.namedtuple("Tuple_dn_getLog", ['RC'])

    ##
    # The getLog command retrieves diagnostic logs from the manager or a mote specified by MAC address.
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getLog named tuple.
    # 
    def dn_getLog(self, macAddress) :
        res = IpMgrConnectorMuxInternal.send(self, ['getLog'], {"macAddress" : macAddress})
        return IpMgrConnectorMux.Tuple_dn_getLog(**res)

    ##
    # The named tuple returned by the dn_sendData() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_sendData = collections.namedtuple("Tuple_dn_sendData", ['RC', 'callbackId'])

    ##
    # The sendData command sends a packet to a mote in the network. The response contains a callbackId. When the manager injects the packet into the network, it will generate a packetSent notification. It is the application layers responsibility send a response from the mote, and to timeout if no response is received.
    # 
    # The sendData command should be used by applications that communicate directly with the manager. If end-to-end (application to mote) IP connectivity is required, the application should use the sendIP command. For a more comprehensive discussion of the distinction, see the SmartMesh IPNetwork User Guide.
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # \param priority 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: Low
    #      - 1: Medium
    #      - 2: High
    # \param srcPort 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param dstPort 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param options 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param data None-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_sendData named tuple.
    # 
    def dn_sendData(self, macAddress, priority, srcPort, dstPort, options, data) :
        res = IpMgrConnectorMuxInternal.send(self, ['sendData'], {"macAddress" : macAddress, "priority" : priority, "srcPort" : srcPort, "dstPort" : dstPort, "options" : options, "data" : data})
        return IpMgrConnectorMux.Tuple_dn_sendData(**res)

    ##
    # The named tuple returned by the dn_startNetwork() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_startNetwork = collections.namedtuple("Tuple_dn_startNetwork", ['RC'])

    ##
    # The startNetwork command tells the manager to allow the network to start forming (begin accepting join requests from devices). The external application must issue the startNetwork command if the autoStartNetwork flag is not set (seesetNetworkConfig). 
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_startNetwork named tuple.
    # 
    def dn_startNetwork(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['startNetwork'], {})
        return IpMgrConnectorMux.Tuple_dn_startNetwork(**res)

    ##
    # The named tuple returned by the dn_getSystemInfo() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>macAddress</tt>: 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>hwModel</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>hwRev</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>swMajor</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>swMinor</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>swPatch</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>swBuild</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getSystemInfo = collections.namedtuple("Tuple_dn_getSystemInfo", ['RC', 'macAddress', 'hwModel', 'hwRev', 'swMajor', 'swMinor', 'swPatch', 'swBuild'])

    ##
    # The getSystemInfo command returns system-level information about the hardware and software versions.
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getSystemInfo named tuple.
    # 
    def dn_getSystemInfo(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['getSystemInfo'], {})
        return IpMgrConnectorMux.Tuple_dn_getSystemInfo(**res)

    ##
    # The named tuple returned by the dn_getMoteConfig() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>macAddress</tt>: 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>isAP</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>state</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: lost
    #      - 1: negotiating
    #      - 4: operational
    # - <tt>reserved</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>isRouting</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getMoteConfig = collections.namedtuple("Tuple_dn_getMoteConfig", ['RC', 'macAddress', 'moteId', 'isAP', 'state', 'reserved', 'isRouting'])

    ##
    # 
    # 
    # The getMoteConfig command returns a single mote description as the response. The command takes two arguments, a MAC Address and a flag indicating whether the MAC Address refers to the requested mote or to the next mote in managers memory. This command may be used to iterate through all motes known by the manager by starting with the macAddress parameter set to 0 and next set to true, and then using the MAC Address of that response as the input to the next call.
    # 
    # The mote MAC address is used in all query commands, but space constraints require the neighbor health reports to use the Mote ID for identification. Therefore, both identifiers are present in the mote structure.
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # \param next 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getMoteConfig named tuple.
    # 
    def dn_getMoteConfig(self, macAddress, next) :
        res = IpMgrConnectorMuxInternal.send(self, ['getMoteConfig'], {"macAddress" : macAddress, "next" : next})
        return IpMgrConnectorMux.Tuple_dn_getMoteConfig(**res)

    ##
    # The named tuple returned by the dn_getPathInfo() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>source</tt>: 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>dest</tt>: 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>direction</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: none
    #      - 1: unused
    #      - 2: upstream
    #      - 3: downstream
    # - <tt>numLinks</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>quality</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>rssiSrcDest</tt>: 1-byte field formatted as a ints.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>rssiDestSrc</tt>: 1-byte field formatted as a ints.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getPathInfo = collections.namedtuple("Tuple_dn_getPathInfo", ['RC', 'source', 'dest', 'direction', 'numLinks', 'quality', 'rssiSrcDest', 'rssiDestSrc'])

    ##
    # The getPathInfo command returns parameters of requested path.
    # 
    # \param source 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # \param dest 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getPathInfo named tuple.
    # 
    def dn_getPathInfo(self, source, dest) :
        res = IpMgrConnectorMuxInternal.send(self, ['getPathInfo'], {"source" : source, "dest" : dest})
        return IpMgrConnectorMux.Tuple_dn_getPathInfo(**res)

    ##
    # The named tuple returned by the dn_getNextPathInfo() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>pathId</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>source</tt>: 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>dest</tt>: 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>direction</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: none
    #      - 1: unused
    #      - 2: upstream
    #      - 3: downstream
    # - <tt>numLinks</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>quality</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>rssiSrcDest</tt>: 1-byte field formatted as a ints.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>rssiDestSrc</tt>: 1-byte field formatted as a ints.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getNextPathInfo = collections.namedtuple("Tuple_dn_getNextPathInfo", ['RC', 'pathId', 'source', 'dest', 'direction', 'numLinks', 'quality', 'rssiSrcDest', 'rssiDestSrc'])

    ##
    # 
    # 
    # The getNextPathInfo command allows iteration across paths connected to a particular mote. The pathId parameter indicates the previous value in the iteration. Setting pathId to 0 returns the first path. A pathId can not be used as a unique identifier for a path. It is only valid when associated with a particular mote. 
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # \param filter 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: all
    #      - 1: upstream
    # \param pathId 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getNextPathInfo named tuple.
    # 
    def dn_getNextPathInfo(self, macAddress, filter, pathId) :
        res = IpMgrConnectorMuxInternal.send(self, ['getNextPathInfo'], {"macAddress" : macAddress, "filter" : filter, "pathId" : pathId})
        return IpMgrConnectorMux.Tuple_dn_getNextPathInfo(**res)

    ##
    # The named tuple returned by the dn_setAdvertising() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_setAdvertising = collections.namedtuple("Tuple_dn_setAdvertising", ['RC', 'callbackId'])

    ##
    # The setAdvertising command tells the manager to activate or deactivate advertising. The response is acallbackId. A commandFinished notification with thecallbackId is generated when the command propagation is complete.
    # 
    # \param activate 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: on
    #      - 1: off
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setAdvertising named tuple.
    # 
    def dn_setAdvertising(self, activate) :
        res = IpMgrConnectorMuxInternal.send(self, ['setAdvertising'], {"activate" : activate})
        return IpMgrConnectorMux.Tuple_dn_setAdvertising(**res)

    ##
    # The named tuple returned by the dn_setDownstreamFrameMode() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_setDownstreamFrameMode = collections.namedtuple("Tuple_dn_setDownstreamFrameMode", ['RC', 'callbackId'])

    ##
    # The setDownstreaFrameMode command tells the manager to shorten or extend the downstream frame. Once this command is executed, the manager switches to manual mode and no longer changes frame size automatically. The response is acallbackId. A commandFinished notification with the callbackId is generated when the command propagation is complete. 
    # 
    # \param frameMode 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: normal
    #      - 1: fast
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setDownstreamFrameMode named tuple.
    # 
    def dn_setDownstreamFrameMode(self, frameMode) :
        res = IpMgrConnectorMuxInternal.send(self, ['setDownstreamFrameMode'], {"frameMode" : frameMode})
        return IpMgrConnectorMux.Tuple_dn_setDownstreamFrameMode(**res)

    ##
    # The named tuple returned by the dn_getManagerStatistics() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>serTxCnt</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>serRxCnt</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>serRxCRCErr</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>serRxOverruns</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>apiEstabConn</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>apiDroppedConn</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>apiTxOk</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>apiTxErr</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>apiTxFail</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>apiRxOk</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>apiRxProtErr</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getManagerStatistics = collections.namedtuple("Tuple_dn_getManagerStatistics", ['RC', 'serTxCnt', 'serRxCnt', 'serRxCRCErr', 'serRxOverruns', 'apiEstabConn', 'apiDroppedConn', 'apiTxOk', 'apiTxErr', 'apiTxFail', 'apiRxOk', 'apiRxProtErr'])

    ##
    # The getManagerStatistics command returns dynamic information and statistics about the manager API. The statistics counts are cleared together with all current statistics using clearStatistics.
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getManagerStatistics named tuple.
    # 
    def dn_getManagerStatistics(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['getManagerStatistics'], {})
        return IpMgrConnectorMux.Tuple_dn_getManagerStatistics(**res)

    ##
    # The named tuple returned by the dn_setTime() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_setTime = collections.namedtuple("Tuple_dn_setTime", ['RC'])

    ##
    # 
    # 
    # The setTime command sets the UTC time on the manager. This command may only be executed when the network is not running. If the trigger flag is false, the manager sets the specified time as soon as it receives the setTime command. When the manager receives a Time Pin trigger, it temporarily stores the current time. If a setTime request is received within a short period of time following the trigger, the manager calculates the delay since the trigger and adjust the time such that the trigger was received at the specified time value.
    # 
    # \param trigger 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param utcSecs 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param utcUsecs 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setTime named tuple.
    # 
    def dn_setTime(self, trigger, utcSecs, utcUsecs) :
        res = IpMgrConnectorMuxInternal.send(self, ['setTime'], {"trigger" : trigger, "utcSecs" : utcSecs, "utcUsecs" : utcUsecs})
        return IpMgrConnectorMux.Tuple_dn_setTime(**res)

    ##
    # The named tuple returned by the dn_getLicense() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>license</tt>: 13-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getLicense = collections.namedtuple("Tuple_dn_getLicense", ['RC', 'license'])

    ##
    # The getLicense command returns the current license key.
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getLicense named tuple.
    # 
    def dn_getLicense(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['getLicense'], {})
        return IpMgrConnectorMux.Tuple_dn_getLicense(**res)

    ##
    # The named tuple returned by the dn_setLicense() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_setLicense = collections.namedtuple("Tuple_dn_setLicense", ['RC'])

    ##
    # The setLicense command validates and updates the software license key stored in flash. Features enabled or disabled by the license key change will take effect after the device is restarted.If the license parameter is set to all 0x0s, the manager restores the default license.
    # 
    # \param license 13-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setLicense named tuple.
    # 
    def dn_setLicense(self, license) :
        res = IpMgrConnectorMuxInternal.send(self, ['setLicense'], {"license" : license})
        return IpMgrConnectorMux.Tuple_dn_setLicense(**res)

    ##
    # The named tuple returned by the dn_setCLIUser() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_setCLIUser = collections.namedtuple("Tuple_dn_setCLIUser", ['RC'])

    ##
    # 
    # 
    # The setUser command sets the password that must be used to log into the command line for a particular user role. The user roles are:
    # 
    # -Viewer - read-only access to non-sensitive information
    # -User - read-write access
    # 
    # \param role 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: viewer
    #      - 1: user
    # \param password 16-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setCLIUser named tuple.
    # 
    def dn_setCLIUser(self, role, password) :
        res = IpMgrConnectorMuxInternal.send(self, ['setCLIUser'], {"role" : role, "password" : password})
        return IpMgrConnectorMux.Tuple_dn_setCLIUser(**res)

    ##
    # The named tuple returned by the dn_sendIP() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_sendIP = collections.namedtuple("Tuple_dn_sendIP", ['RC', 'callbackId'])

    ##
    # The sendIP command sends an 6LowPAN packet to a mote in the network. The response contains a callbackId. When the manager injects the packet into the network, it will generate a packetSent notification. It is the application layers responsibility send a response from the mote, and to timeout if no response is received. The application is responsible for constructing a valid 6LoWPAN packet.
    # 
    # The sendIP command should be used by applications that require end-to-end IP connectivity. For applications that do not require end-to-end IP connectivity, the sendData command provides a simpler interface without requiring the application to understand 6LoWPAN encapsulation. For a more comprehensive discussion of the distinction, see theSmartMesh IP Network User Guide.
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # \param priority 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: Low
    #      - 1: Medium
    #      - 2: High
    # \param options 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param encryptedOffset 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param data None-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_sendIP named tuple.
    # 
    def dn_sendIP(self, macAddress, priority, options, encryptedOffset, data) :
        res = IpMgrConnectorMuxInternal.send(self, ['sendIP'], {"macAddress" : macAddress, "priority" : priority, "options" : options, "encryptedOffset" : encryptedOffset, "data" : data})
        return IpMgrConnectorMux.Tuple_dn_sendIP(**res)

    ##
    # The named tuple returned by the dn_startLocation() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_startLocation = collections.namedtuple("Tuple_dn_startLocation", ['RC', 'callbackId'])

    ##
    # 
    # 
    # The startLocation command sends a request to a set of motes to generate distance measurements to a mobile mote. The manager sends a series of commands to the specified motes active the location links for enough time to perform the requested measurements. More than one startLocation request may be queued up by the manager, but the queue size is limited. The caller must be able to handle a queue full error and retry. The startLocation request contains a variable number of fixed motes. The manager determines the number of fixedMotes provided by the caller by checking the length of the request. 
    # 
    # 
    # 
    # The startLocation call returns acallbackId that is used to inform the caller of the progress of the distance measurement (seeEvent Notifications). Location events are similar to commandFinished events. The distance measurements are returned as ipData notificationsfrom the fixed motes. The startLocation command is only allowed if the licenseallows it.
    # 
    # \param numMeasurements 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param mobileMote 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # \param fixedMotes None-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_startLocation named tuple.
    # 
    def dn_startLocation(self, numMeasurements, mobileMote, fixedMotes) :
        res = IpMgrConnectorMuxInternal.send(self, ['startLocation'], {"numMeasurements" : numMeasurements, "mobileMote" : mobileMote, "fixedMotes" : fixedMotes})
        return IpMgrConnectorMux.Tuple_dn_startLocation(**res)

    ##
    # The named tuple returned by the dn_restoreFactoryDefaults() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_restoreFactoryDefaults = collections.namedtuple("Tuple_dn_restoreFactoryDefaults", ['RC'])

    ##
    # The restoreFactoryDefaults command restores the default configuration and clears the ACL. This command does not affect the license.
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_restoreFactoryDefaults named tuple.
    # 
    def dn_restoreFactoryDefaults(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['restoreFactoryDefaults'], {})
        return IpMgrConnectorMux.Tuple_dn_restoreFactoryDefaults(**res)

    ##
    # The named tuple returned by the dn_getMoteInfo() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>macAddress</tt>: 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>state</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: lost
    #      - 1: negotiating
    #      - 4: operational
    # - <tt>numNbrs</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>numGoodNbrs</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>requestedBw</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>totalNeededBw</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>assignedBw</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>packetsReceived</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>packetsLost</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>avgLatency</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getMoteInfo = collections.namedtuple("Tuple_dn_getMoteInfo", ['RC', 'macAddress', 'state', 'numNbrs', 'numGoodNbrs', 'requestedBw', 'totalNeededBw', 'assignedBw', 'packetsReceived', 'packetsLost', 'avgLatency'])

    ##
    # The getMoteInfo command returns dynamic information for the specified mote. 
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getMoteInfo named tuple.
    # 
    def dn_getMoteInfo(self, macAddress) :
        res = IpMgrConnectorMuxInternal.send(self, ['getMoteInfo'], {"macAddress" : macAddress})
        return IpMgrConnectorMux.Tuple_dn_getMoteInfo(**res)

    ##
    # The named tuple returned by the dn_getNetworkConfig() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>networkId</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>apTxPower</tt>: 1-byte field formatted as a ints.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>frameProfile</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 1: Profile_01
    # - <tt>maxMotes</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>baseBandwidth</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>downFrameMultVal</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>numParents</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>ccaMode</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: off
    #      - 1: energy
    #      - 2: carrier
    #      - 3: both
    # - <tt>channelList</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>autoStartNetwork</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>locMode</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: off
    #      - 1: onDemand
    # - <tt>bbMode</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: off
    #      - 1: upstream
    #      - 2: bidirectional
    # - <tt>bbSize</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>isRadioTest</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>bwMult</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>oneChannel</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getNetworkConfig = collections.namedtuple("Tuple_dn_getNetworkConfig", ['RC', 'networkId', 'apTxPower', 'frameProfile', 'maxMotes', 'baseBandwidth', 'downFrameMultVal', 'numParents', 'ccaMode', 'channelList', 'autoStartNetwork', 'locMode', 'bbMode', 'bbSize', 'isRadioTest', 'bwMult', 'oneChannel'])

    ##
    # The getNetworkConfig command returns general network configuration parameters, including the Network ID, bandwidth parameters and number of motes.
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getNetworkConfig named tuple.
    # 
    def dn_getNetworkConfig(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['getNetworkConfig'], {})
        return IpMgrConnectorMux.Tuple_dn_getNetworkConfig(**res)

    ##
    # The named tuple returned by the dn_getNetworkInfo() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>numMotes</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>asnSize</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>advertisementState</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: on
    #      - 1: off
    # - <tt>downFrameState</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: normal
    #      - 1: fast
    # - <tt>netReliability</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>netPathStability</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>netLatency</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>netState</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: operational
    #      - 1: radiotest
    #      - 2: notStarted
    #      - 3: errorStartup
    #      - 4: errorConfig
    #      - 5: errorLicense
    # - <tt>ipv6Address</tt>: 16-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getNetworkInfo = collections.namedtuple("Tuple_dn_getNetworkInfo", ['RC', 'numMotes', 'asnSize', 'advertisementState', 'downFrameState', 'netReliability', 'netPathStability', 'netLatency', 'netState', 'ipv6Address'])

    ##
    # The getNetworkInfo command returns dynamic network information and statistics.
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getNetworkInfo named tuple.
    # 
    def dn_getNetworkInfo(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['getNetworkInfo'], {})
        return IpMgrConnectorMux.Tuple_dn_getNetworkInfo(**res)

    ##
    # The named tuple returned by the dn_getMoteConfigById() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>macAddress</tt>: 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>isAP</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>state</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: lost
    #      - 1: negotiating
    #      - 4: operational
    # - <tt>reserved</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>isRouting</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getMoteConfigById = collections.namedtuple("Tuple_dn_getMoteConfigById", ['RC', 'macAddress', 'moteId', 'isAP', 'state', 'reserved', 'isRouting'])

    ##
    # The getMoteConfigById command returns a single mote description as the response. The command takes one argument, the short address of a mote (Mote ID). The command returns the same response structure as the getMoteConfig command.
    # 
    # \param moteId 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getMoteConfigById named tuple.
    # 
    def dn_getMoteConfigById(self, moteId) :
        res = IpMgrConnectorMuxInternal.send(self, ['getMoteConfigById'], {"moteId" : moteId})
        return IpMgrConnectorMux.Tuple_dn_getMoteConfigById(**res)

    ##
    # The named tuple returned by the dn_setCommonJoinKey() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_setCommonJoinKey = collections.namedtuple("Tuple_dn_setCommonJoinKey", ['RC'])

    ##
    # The setCommonJoinKey command will set a new value for the common join key. The common join key is used to decrypt join messages only if the ACL is empty.
    # 
    # \param key 16-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setCommonJoinKey named tuple.
    # 
    def dn_setCommonJoinKey(self, key) :
        res = IpMgrConnectorMuxInternal.send(self, ['setCommonJoinKey'], {"key" : key})
        return IpMgrConnectorMux.Tuple_dn_setCommonJoinKey(**res)

    ##
    # The named tuple returned by the dn_getIPConfig() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>ipv6Address</tt>: 16-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>mask</tt>: 16-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getIPConfig = collections.namedtuple("Tuple_dn_getIPConfig", ['RC', 'ipv6Address', 'mask'])

    ##
    # The getIPConfig command returns the manager's IP configuration parameters, including the IPv6 address and mask.
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getIPConfig named tuple.
    # 
    def dn_getIPConfig(self, ) :
        res = IpMgrConnectorMuxInternal.send(self, ['getIPConfig'], {})
        return IpMgrConnectorMux.Tuple_dn_getIPConfig(**res)

    ##
    # The named tuple returned by the dn_setIPConfig() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_setIPConfig = collections.namedtuple("Tuple_dn_setIPConfig", ['RC'])

    ##
    # The setIPConfig command sets the manager's IP configuration parameters, including the IPv6 address and mask.
    # 
    # \param ipv6Address 16-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # \param mask 16-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setIPConfig named tuple.
    # 
    def dn_setIPConfig(self, ipv6Address, mask) :
        res = IpMgrConnectorMuxInternal.send(self, ['setIPConfig'], {"ipv6Address" : ipv6Address, "mask" : mask})
        return IpMgrConnectorMux.Tuple_dn_setIPConfig(**res)

    ##
    # The named tuple returned by the dn_deleteMote() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # 
    Tuple_dn_deleteMote = collections.namedtuple("Tuple_dn_deleteMote", ['RC'])

    ##
    # The deleteMote command deletes a mote from the manager's list. A mote can only be deleted if it in the Lost or Unknown states. 
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_deleteMote named tuple.
    # 
    def dn_deleteMote(self, macAddress) :
        res = IpMgrConnectorMuxInternal.send(self, ['deleteMote'], {"macAddress" : macAddress})
        return IpMgrConnectorMux.Tuple_dn_deleteMote(**res)

    ##
    # The named tuple returned by the dn_getMoteLinks() function.
    # 
    # - <tt>RC</tt>: 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: RC_OK
    #      - 1: RC_INVALID_COMMAND
    #      - 2: RC_INVALID_ARGUMENT
    #      - 3: INVALID_AUTHENTICATION
    #      - 4: INVALID_API_VERSION
    #      - 5: comd_timeout
    #      - 11: RC_END_OF_LIST
    #      - 12: RC_NO_RESOURCES
    #      - 13: RC_IN_PROGRESS
    #      - 14: RC_NACK
    #      - 15: RC_WRITE_FAIL
    #      - 16: RC_VALIDATION_ERROR
    # - <tt>idx</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>utilization</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>numLinks</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>frameId_1</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>slot_1</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>channelOffset_1</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId_1</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>flags_1</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>frameId_2</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>slot_2</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>channelOffset_2</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId_2</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>flags_2</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>frameId_3</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>slot_3</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>channelOffset_3</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId_3</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>flags_3</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>frameId_4</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>slot_4</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>channelOffset_4</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId_4</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>flags_4</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>frameId_5</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>slot_5</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>channelOffset_5</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId_5</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>flags_5</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>frameId_6</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>slot_6</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>channelOffset_6</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId_6</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>flags_6</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>frameId_7</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>slot_7</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>channelOffset_7</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId_7</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>flags_7</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>frameId_8</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>slot_8</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>channelOffset_8</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId_8</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>flags_8</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>frameId_9</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>slot_9</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>channelOffset_9</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId_9</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>flags_9</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>frameId_10</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>slot_10</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>channelOffset_10</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteId_10</tt>: 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>flags_10</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getMoteLinks = collections.namedtuple("Tuple_dn_getMoteLinks", ['RC', 'idx', 'utilization', 'numLinks', 'frameId_1', 'slot_1', 'channelOffset_1', 'moteId_1', 'flags_1', 'frameId_2', 'slot_2', 'channelOffset_2', 'moteId_2', 'flags_2', 'frameId_3', 'slot_3', 'channelOffset_3', 'moteId_3', 'flags_3', 'frameId_4', 'slot_4', 'channelOffset_4', 'moteId_4', 'flags_4', 'frameId_5', 'slot_5', 'channelOffset_5', 'moteId_5', 'flags_5', 'frameId_6', 'slot_6', 'channelOffset_6', 'moteId_6', 'flags_6', 'frameId_7', 'slot_7', 'channelOffset_7', 'moteId_7', 'flags_7', 'frameId_8', 'slot_8', 'channelOffset_8', 'moteId_8', 'flags_8', 'frameId_9', 'slot_9', 'channelOffset_9', 'moteId_9', 'flags_9', 'frameId_10', 'slot_10', 'channelOffset_10', 'moteId_10', 'flags_10'])

    ##
    # ThegetMoteLinkscommand returns information about links assigned to the mote. The response contains a list of links starting with Nth link on the mote, where N is supplied as theidxparameter in the request. To retrieve all links on the device the user can call this command withidxthat increments by number of links returned with priorresponse, until the command returns RC_END_OF_LIST response code. Note that links assigned to a mote may change between API calls.
    # 
    # \param macAddress 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # \param idx 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getMoteLinks named tuple.
    # 
    def dn_getMoteLinks(self, macAddress, idx) :
        res = IpMgrConnectorMuxInternal.send(self, ['getMoteLinks'], {"macAddress" : macAddress, "idx" : idx})
        return IpMgrConnectorMux.Tuple_dn_getMoteLinks(**res)

    #======================== notifications ===================================
    
    ##
    # Dictionary of all notification tuples.
    #
    notifTupleTable = {}
    
    ##
    # \brief MANAGER_HELLO notification.
    # 
    # Sent by the manager to a initiate new session with a client.
    #
    # Formatted as a Tuple_manager_hello named tuple. It contains the following fields:
    #   - <tt>version</tt> 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>mode</tt> 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    MANAGER_HELLO = "manager_hello"
    notifTupleTable[MANAGER_HELLO] = Tuple_manager_hello = collections.namedtuple("Tuple_manager_hello", ['version', 'mode'])

    ##
    # \brief EVENTMOTERESET notification.
    # 
    # This notification is sent when a user-initiated reset is executed by the manager.
    #
    # Formatted as a Tuple_eventMoteReset named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddress</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.    
    # 
    EVENTMOTERESET = "eventMoteReset"
    notifTupleTable[EVENTMOTERESET] = Tuple_eventMoteReset = collections.namedtuple("Tuple_eventMoteReset", ['eventId', 'macAddress'])

    ##
    # \brief EVENTNETWORKRESET notification.
    # 
    # This notification is sent when the manager starts the network. This event has no eventData fields.
    #
    # Formatted as a Tuple_eventNetworkReset named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    EVENTNETWORKRESET = "eventNetworkReset"
    notifTupleTable[EVENTNETWORKRESET] = Tuple_eventNetworkReset = collections.namedtuple("Tuple_eventNetworkReset", ['eventId'])

    ##
    # \brief EVENTCOMMANDFINISH notification.
    # 
    # The commandFinished notification is used when a reliable command response is received.
    #
    # Formatted as a Tuple_eventCommandFinish named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>callbackId</tt> 4-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>rc</tt> 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: OK
    #      - 1: nack
    #      - 2: commandTimeout    
    # 
    EVENTCOMMANDFINISH = "eventCommandFinish"
    notifTupleTable[EVENTCOMMANDFINISH] = Tuple_eventCommandFinish = collections.namedtuple("Tuple_eventCommandFinish", ['eventId', 'callbackId', 'rc'])

    ##
    # \brief EVENTMOTEJOIN notification.
    # 
    # This notification is sent when a mote joins the network.
    #
    # Formatted as a Tuple_eventMoteJoin named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddress</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.    
    # 
    EVENTMOTEJOIN = "eventMoteJoin"
    notifTupleTable[EVENTMOTEJOIN] = Tuple_eventMoteJoin = collections.namedtuple("Tuple_eventMoteJoin", ['eventId', 'macAddress'])

    ##
    # \brief EVENTMOTEOPERATIONAL notification.
    # 
    # This notification is sent when a mote that joins the network becomes operational.
    #
    # Formatted as a Tuple_eventMoteOperational named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddress</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.    
    # 
    EVENTMOTEOPERATIONAL = "eventMoteOperational"
    notifTupleTable[EVENTMOTEOPERATIONAL] = Tuple_eventMoteOperational = collections.namedtuple("Tuple_eventMoteOperational", ['eventId', 'macAddress'])

    ##
    # \brief EVENTMOTELOST notification.
    # 
    # This notification is sent when a mote's state changes to "Lost," which may occur when a mote becomes unreachable through the network.
    #
    # Formatted as a Tuple_eventMoteLost named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddress</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.    
    # 
    EVENTMOTELOST = "eventMoteLost"
    notifTupleTable[EVENTMOTELOST] = Tuple_eventMoteLost = collections.namedtuple("Tuple_eventMoteLost", ['eventId', 'macAddress'])

    ##
    # \brief EVENTNETTIME notification.
    # 
    # The time notification is triggered by the client asserting the TIME pin or by calling the getTime command. This notification contains the time when the TIME pin was asserted (or the getTime command was processed) expressed as:
    # 
    # - ASN--The absolute slot number (the number of timeslots since 20:00:00 UTC July 2,2002 if UTC is set on manager, otherwise since Jan 1, 1970)
    # - Uptime--The number of seconds since the device was booted
    # -- Unix time--The number of seconds and microseconds since Jan 1, 1970 in UTC
    #
    # Formatted as a Tuple_eventNetTime named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>uptime</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>utcSecs</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>utcUsecs</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>asn</tt> 5-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>asnOffset</tt> 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    EVENTNETTIME = "eventNetTime"
    notifTupleTable[EVENTNETTIME] = Tuple_eventNetTime = collections.namedtuple("Tuple_eventNetTime", ['eventId', 'uptime', 'utcSecs', 'utcUsecs', 'asn', 'asnOffset'])

    ##
    # \brief EVENTPINGRESPONSE notification.
    # 
    # This notification is sent when a reply is received from a mote ping.
    #
    # Formatted as a Tuple_eventPingResponse named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>callbackId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddress</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>delay</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>voltage</tt> 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>temperature</tt> 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    EVENTPINGRESPONSE = "eventPingResponse"
    notifTupleTable[EVENTPINGRESPONSE] = Tuple_eventPingResponse = collections.namedtuple("Tuple_eventPingResponse", ['eventId', 'callbackId', 'macAddress', 'delay', 'voltage', 'temperature'])

    ##
    # \brief EVENTPATHCREATE notification.
    # 
    # This notification is sent when the manager creates a connection (path) between two motes.
    #
    # Formatted as a Tuple_eventPathCreate named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>source</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>dest</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>direction</tt> 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: none
    #      - 1: unused
    #      - 2: upstream
    #      - 3: downstream    
    # 
    EVENTPATHCREATE = "eventPathCreate"
    notifTupleTable[EVENTPATHCREATE] = Tuple_eventPathCreate = collections.namedtuple("Tuple_eventPathCreate", ['eventId', 'source', 'dest', 'direction'])

    ##
    # \brief EVENTPATHDELETE notification.
    # 
    # This notification is sent when the manager removes a connection (path) between two motes.
    #
    # Formatted as a Tuple_eventPathDelete named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>source</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>dest</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>direction</tt> 1-byte field formatted as a int.<br/>
    #     This field can only take one of the following values:
    #      - 0: none
    #      - 1: unused
    #      - 2: upstream
    #      - 3: downstream    
    # 
    EVENTPATHDELETE = "eventPathDelete"
    notifTupleTable[EVENTPATHDELETE] = Tuple_eventPathDelete = collections.namedtuple("Tuple_eventPathDelete", ['eventId', 'source', 'dest', 'direction'])

    ##
    # \brief EVENTPACKETSENT notification.
    # 
    # The packetSent notification is generated when client's packet is removed from manager's queue and sent into the wireless network.
    #
    # Formatted as a Tuple_eventPacketSent named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>callbackId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>rc</tt> 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    EVENTPACKETSENT = "eventPacketSent"
    notifTupleTable[EVENTPACKETSENT] = Tuple_eventPacketSent = collections.namedtuple("Tuple_eventPacketSent", ['eventId', 'callbackId', 'rc'])

    ##
    # \brief EVENTMOTECREATE notification.
    # 
    # This event is sent when a mote joins the manager for the first time.
    #
    # Formatted as a Tuple_eventMoteCreate named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddress</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteId</tt> 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    EVENTMOTECREATE = "eventMoteCreate"
    notifTupleTable[EVENTMOTECREATE] = Tuple_eventMoteCreate = collections.namedtuple("Tuple_eventMoteCreate", ['eventId', 'macAddress', 'moteId'])

    ##
    # \brief EVENTMOTEDELETE notification.
    # 
    # This notification is sent when a mote is deleted as a result of moteDelete command.
    #
    # Formatted as a Tuple_eventMoteDelete named tuple. It contains the following fields:
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddress</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteId</tt> 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    EVENTMOTEDELETE = "eventMoteDelete"
    notifTupleTable[EVENTMOTEDELETE] = Tuple_eventMoteDelete = collections.namedtuple("Tuple_eventMoteDelete", ['eventId', 'macAddress', 'moteId'])

    ##
    # \brief NOTIFLOG notification.
    # 
    # Log notification
    #
    # Formatted as a Tuple_notifLog named tuple. It contains the following fields:
    #   - <tt>macAddress</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>logMsg</tt> None-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.    
    # 
    NOTIFLOG = "notifLog"
    notifTupleTable[NOTIFLOG] = Tuple_notifLog = collections.namedtuple("Tuple_notifLog", ['macAddress', 'logMsg'])

    ##
    # \brief NOTIFDATA notification.
    # 
    # Data payload notification
    #
    # Formatted as a Tuple_notifData named tuple. It contains the following fields:
    #   - <tt>utcSecs</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>utcUsecs</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddress</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>srcPort</tt> 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>dstPort</tt> 2-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>data</tt> None-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.    
    # 
    NOTIFDATA = "notifData"
    notifTupleTable[NOTIFDATA] = Tuple_notifData = collections.namedtuple("Tuple_notifData", ['utcSecs', 'utcUsecs', 'macAddress', 'srcPort', 'dstPort', 'data'])

    ##
    # \brief NOTIFIPDATA notification.
    # 
    # 6lowpan packet notification
    #
    # Formatted as a Tuple_notifIpData named tuple. It contains the following fields:
    #   - <tt>utcSecs</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>utcUsecs</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddress</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>data</tt> None-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.    
    # 
    NOTIFIPDATA = "notifIpData"
    notifTupleTable[NOTIFIPDATA] = Tuple_notifIpData = collections.namedtuple("Tuple_notifIpData", ['utcSecs', 'utcUsecs', 'macAddress', 'data'])

    ##
    # \brief NOTIFHEALTHREPORT notification.
    # 
    # Health report notification
    #
    # Formatted as a Tuple_notifHealthReport named tuple. It contains the following fields:
    #   - <tt>macAddress</tt> 8-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>payload</tt> None-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.    
    # 
    NOTIFHEALTHREPORT = "notifHealthReport"
    notifTupleTable[NOTIFHEALTHREPORT] = Tuple_notifHealthReport = collections.namedtuple("Tuple_notifHealthReport", ['macAddress', 'payload'])

    ##
    # \brief Get a notification from the notification queue, and returns
    #        it properly formatted.
    #
    # \exception NotificationError if unknown notification.
    # 
    def getNotification(self, timeoutSec=-1) :
        temp = self.getNotificationInternal(timeoutSec)
        if not temp:
            return temp
        (ids, param) = temp
        try :
            if  IpMgrConnectorMux.notifTupleTable[ids[-1]] :
                return (ids[-1], IpMgrConnectorMux.notifTupleTable[ids[-1]](**param))
            else :
                return (ids[-1], None)
        except KeyError :
            raise ApiException.NotificationError(ids, param)
