## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    module = bld.create_ns3_module('applications', ['internet', 'config-store','stats'])
    module.source = [
        'model/bulk-send-application.cc',
        'model/onoff-application.cc',
        'model/packet-sink.cc',
        'model/udp-client.cc',
        'model/udp-server.cc',
        'model/seq-ts-header.cc',
        'model/udp-trace-client.cc',
        'model/packet-loss-counter.cc',
        'model/udp-echo-client.cc',
        'model/udp-echo-server.cc',
        'model/adaptation-algorithms/tcp-stream-client.cc',
        'model/adaptation-algorithms/tcp-stream-server.cc',
        'model/adaptation-algorithms/tcp-stream-adaptation-algorithm.cc',
        'model/adaptation-algorithms/festive.cc',
        'model/adaptation-algorithms/panda.cc',
        'model/adaptation-algorithms/tobasco2.cc',
        'model/application-packet-probe.cc',
        'helper/bulk-send-helper.cc',
        'helper/on-off-helper.cc',
        'helper/packet-sink-helper.cc',
        'helper/udp-client-server-helper.cc',
        'helper/udp-echo-helper.cc',
        'helper/tcp-stream-helper.cc',
        ]

    applications_test = bld.create_ns3_module_test_library('applications')
    applications_test.source = [
        'test/udp-client-server-test.cc',
        ]

    headers = bld(features='ns3header')
    headers.module = 'applications'
    headers.source = [
        'model/bulk-send-application.h',
        'model/onoff-application.h',
        'model/packet-sink.h',
        'model/udp-client.h',
        'model/udp-server.h',
        'model/seq-ts-header.h',
        'model/udp-trace-client.h',
        'model/packet-loss-counter.h',
        'model/udp-echo-client.h',
        'model/udp-echo-server.h',
        'model/adaptation-algorithms/tcp-stream-client.h',
        'model/adaptation-algorithms/tcp-stream-server.h',
        'model/adaptation-algorithms/tcp-stream-interface.h',
        'model/adaptation-algorithms/tcp-stream-adaptation-algorithm.h',
        'model/adaptation-algorithms/festive.h',
        'model/adaptation-algorithms/panda.h',
        'model/adaptation-algorithms/tobasco2.h',
        'model/application-packet-probe.h',
        'helper/tcp-stream-helper.h',
        'helper/bulk-send-helper.h',
        'helper/on-off-helper.h',
        'helper/packet-sink-helper.h',
        'helper/udp-client-server-helper.h',
        'helper/udp-echo-helper.h',
        ]

    bld.ns3_python_bindings()
