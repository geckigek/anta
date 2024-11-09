# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Tests for anta.tests.routing.bgp.py."""

# pylint: disable=C0302
from __future__ import annotations

from typing import Any

from anta.tests.routing.bgp import (
    VerifyBGPAdvCommunities,
    VerifyBGPExchangedRoutes,
    VerifyBGPPeerASNCap,
    VerifyBGPPeerCount,
    VerifyBGPPeerDropStats,
    VerifyBGPPeerMD5Auth,
    VerifyBGPPeerMPCaps,
    VerifyBGPPeerRouteLimit,
    VerifyBGPPeerRouteRefreshCap,
    VerifyBGPPeersHealth,
    VerifyBGPPeerUpdateErrors,
    VerifyBgpRouteMaps,
    VerifyBGPSpecificPeers,
    VerifyBGPTimers,
    VerifyEVPNType2Route,
)
from tests.units.anta_tests import test

DATA: list[dict[str, Any]] = [
    {
        "name": "success",
        "test": VerifyBGPPeerCount,
        "eos_data": [
            # Need to order the output as the commands would be sorted after template rendering.
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.0": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.2": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peers": {
                            "10.255.0.21": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.255.0.1": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.255.0.2": {
                                "description": "DC1-SPINE2_Ethernet1",
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.255.0.11": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.255.0.12": {
                                "description": "DC1-SPINE2_Ethernet1",
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.255.0.21": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.255.0.22": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
        ],
        "inputs": {
            "address_families": [
                # evpn first to make sure that the correct mapping output to input is kept.
                {"afi": "evpn", "num_peers": 2},
                {"afi": "ipv4", "safi": "unicast", "vrf": "default", "num_peers": 2},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "MGMT", "num_peers": 1},
                {"afi": "link-state", "num_peers": 2},
                {"afi": "path-selection", "num_peers": 2},
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-wrong-count",
        "test": VerifyBGPPeerCount,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.0": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.2": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peers": {
                            "10.255.0.21": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.255.0.1": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.255.0.2": {
                                "description": "DC1-SPINE2_Ethernet1",
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.255.0.11": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.255.0.12": {
                                "description": "DC1-SPINE2_Ethernet1",
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.255.0.21": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
        ],
        "inputs": {
            "address_families": [
                {"afi": "ipv4", "safi": "unicast", "vrf": "default", "num_peers": 3},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "MGMT", "num_peers": 2},
                {"afi": "evpn", "num_peers": 1},
                {"afi": "link-state", "num_peers": 3},
                {"afi": "path-selection", "num_peers": 3},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv4', 'safi': 'unicast', 'vrfs': {'default': 'Expected: 3, Actual: 2'}}, "
                "{'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'MGMT': 'Expected: 2, Actual: 1'}}, "
                "{'afi': 'evpn', 'vrfs': {'default': 'Expected: 1, Actual: 2'}}, "
                "{'afi': 'link-state', 'vrfs': {'default': 'Expected: 3, Actual: 2'}}, "
                "{'afi': 'path-selection', 'vrfs': {'default': 'Expected: 3, Actual: 1'}}]"
            ],
        },
    },
    {
        "name": "failure-no-peers",
        "test": VerifyBGPPeerCount,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peers": {},
                    }
                }
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peers": {},
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {},
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {},
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {},
                    }
                }
            },
        ],
        "inputs": {
            "address_families": [
                {"afi": "ipv4", "safi": "unicast", "vrf": "default", "num_peers": 2},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "MGMT", "num_peers": 1},
                {"afi": "evpn", "num_peers": 2},
                {"afi": "link-state", "num_peers": 2},
                {"afi": "path-selection", "num_peers": 2},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv4', 'safi': 'unicast', 'vrfs': {'default': 'Expected: 2, Actual: 0'}}, "
                "{'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'MGMT': 'Expected: 1, Actual: 0'}}, "
                "{'afi': 'evpn', 'vrfs': {'default': 'Expected: 2, Actual: 0'}}, "
                "{'afi': 'link-state', 'vrfs': {'default': 'Expected: 2, Actual: 0'}}, "
                "{'afi': 'path-selection', 'vrfs': {'default': 'Expected: 2, Actual: 0'}}]"
            ],
        },
    },
    {
        "name": "failure-not-configured",
        "test": VerifyBGPPeerCount,
        "eos_data": [{"vrfs": {}}, {"vrfs": {}}, {"vrfs": {}}, {"vrfs": {}}, {"vrfs": {}}],
        "inputs": {
            "address_families": [
                {"afi": "ipv6", "safi": "multicast", "vrf": "DEV", "num_peers": 3},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "MGMT", "num_peers": 1},
                {"afi": "evpn", "num_peers": 2},
                {"afi": "link-state", "num_peers": 2},
                {"afi": "path-selection", "num_peers": 2},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv6', 'safi': 'multicast', 'vrfs': {'DEV': 'Not Configured'}}, "
                "{'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'MGMT': 'Not Configured'}}, "
                "{'afi': 'evpn', 'vrfs': {'default': 'Not Configured'}}, "
                "{'afi': 'link-state', 'vrfs': {'default': 'Not Configured'}}, "
                "{'afi': 'path-selection', 'vrfs': {'default': 'Not Configured'}}]"
            ],
        },
    },
    {
        "name": "success-vrf-all",
        "test": VerifyBGPPeerCount,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.0": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                    "PROD": {
                        "peers": {
                            "10.1.254.1": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "192.168.1.11": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.10": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                    "PROD": {
                        "peers": {
                            "10.1.254.11": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
        ],
        "inputs": {
            "address_families": [
                {"afi": "ipv4", "safi": "unicast", "vrf": "all", "num_peers": 3},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "all", "num_peers": 2},
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-vrf-all",
        "test": VerifyBGPPeerCount,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.0": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                    "PROD": {
                        "peers": {
                            "10.1.254.1": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "192.168.1.11": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.10": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                    "PROD": {
                        "peers": {
                            "10.1.254.1": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "192.168.1.12": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
        ],
        "inputs": {
            "address_families": [
                {"afi": "ipv4", "safi": "unicast", "vrf": "all", "num_peers": 5},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "all", "num_peers": 2},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv4', 'safi': 'unicast', 'vrfs': {'all': 'Expected: 5, Actual: 3'}}, "
                "{'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'all': 'Expected: 2, Actual: 3'}}]"
            ],
        },
    },
    {
        "name": "failure-multiple-afi",
        "test": VerifyBGPPeerCount,
        "eos_data": [
            {
                "vrfs": {
                    "PROD": {
                        "peers": {
                            "10.1.254.1": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "192.168.1.11": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {"vrfs": {}},
            {
                "vrfs": {
                    "MGMT": {
                        "peers": {
                            "10.1.254.11": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "192.168.1.21": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.0.1": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.0.2": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.0.11": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.0.21": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.0.2": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.0.22": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                },
            },
        ],
        "inputs": {
            "address_families": [
                {"afi": "ipv4", "safi": "unicast", "vrf": "PROD", "num_peers": 3},
                {"afi": "ipv6", "safi": "unicast", "vrf": "default", "num_peers": 3},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "MGMT", "num_peers": 3},
                {"afi": "evpn", "num_peers": 3},
                {"afi": "link-state", "num_peers": 4},
                {"afi": "path-selection", "num_peers": 1},
            ],
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv4', 'safi': 'unicast', 'vrfs': {'PROD': 'Expected: 3, Actual: 2'}}, "
                "{'afi': 'ipv6', 'safi': 'unicast', 'vrfs': {'default': 'Not Configured'}}, "
                "{'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'MGMT': 'Expected: 3, Actual: 2'}}, "
                "{'afi': 'evpn', 'vrfs': {'default': 'Expected: 3, Actual: 2'}}, "
                "{'afi': 'link-state', 'vrfs': {'default': 'Expected: 4, Actual: 2'}}, "
                "{'afi': 'path-selection', 'vrfs': {'default': 'Expected: 1, Actual: 2'}}]",
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPPeersHealth,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.0": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.2": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peers": {
                            "10.1.255.10": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.12": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.20": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.22": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.30": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.32": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
        ],
        "inputs": {
            "address_families": [
                # Path selection first to make sure input to output mapping is correct.
                {"afi": "path-selection"},
                {"afi": "ipv4", "safi": "unicast", "vrf": "default"},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "MGMT"},
                {"afi": "link-state"},
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-issues",
        "test": VerifyBGPPeersHealth,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.0": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Idle",
                            },
                            "10.1.255.2": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peers": {
                            "10.1.255.10": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.12": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Idle",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.20": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Idle",
                            },
                            "10.1.255.22": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.30": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.32": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Idle",
                            },
                        },
                    }
                }
            },
        ],
        "inputs": {
            "address_families": [
                {"afi": "ipv4", "safi": "unicast", "vrf": "default"},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "MGMT"},
                {"afi": "path-selection"},
                {"afi": "link-state"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv4', 'safi': 'unicast', 'vrfs': {'default': {'10.1.255.0': {'peerState': 'Idle', 'inMsgQueue': 0, 'outMsgQueue': 0}}}}, "
                "{'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'MGMT': {'10.1.255.12': {'peerState': 'Idle', 'inMsgQueue': 0, 'outMsgQueue': 0}}}}, "
                "{'afi': 'path-selection', 'vrfs': {'default': {'10.1.255.20': {'peerState': 'Idle', 'inMsgQueue': 0, 'outMsgQueue': 0}}}}, "
                "{'afi': 'link-state', 'vrfs': {'default': {'10.1.255.32': {'peerState': 'Idle', 'inMsgQueue': 0, 'outMsgQueue': 0}}}}]"
            ],
        },
    },
    {
        "name": "success-vrf-all",
        "test": VerifyBGPPeersHealth,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.0": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.2": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                    "PROD": {
                        "peers": {
                            "10.1.254.1": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "192.168.1.11": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.10": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.12": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                    "PROD": {
                        "peers": {
                            "10.1.254.11": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "192.168.1.111": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                }
            },
        ],
        "inputs": {
            "address_families": [
                {"afi": "ipv4", "safi": "unicast", "vrf": "all"},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "all"},
            ]
        },
        "expected": {
            "result": "success",
        },
    },
    {
        "name": "failure-issues-vrf-all",
        "test": VerifyBGPPeersHealth,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.0": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Idle",
                            },
                            "10.1.255.2": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                    "PROD": {
                        "peers": {
                            "10.1.254.1": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "192.168.1.11": {
                                "inMsgQueue": 100,
                                "outMsgQueue": 200,
                                "peerState": "Established",
                            },
                        },
                    },
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.10": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Idle",
                            },
                            "10.1.255.12": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    },
                    "PROD": {
                        "peers": {
                            "10.1.254.11": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "192.168.1.111": {
                                "inMsgQueue": 100,
                                "outMsgQueue": 200,
                                "peerState": "Established",
                            },
                        },
                    },
                }
            },
        ],
        "inputs": {
            "address_families": [
                {"afi": "ipv4", "safi": "unicast", "vrf": "all"},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "all"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv4', 'safi': 'unicast', 'vrfs': {'default': {'10.1.255.0': {'peerState': 'Idle', 'inMsgQueue': 0, 'outMsgQueue': 0}}, "
                "'PROD': {'192.168.1.11': {'peerState': 'Established', 'inMsgQueue': 100, 'outMsgQueue': 200}}}}, "
                "{'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'default': {'10.1.255.10': {'peerState': 'Idle', 'inMsgQueue': 0, 'outMsgQueue': 0}}, "
                "'PROD': {'192.168.1.111': {'peerState': 'Established', 'inMsgQueue': 100, 'outMsgQueue': 200}}}}]"
            ],
        },
    },
    {
        "name": "failure-not-configured",
        "test": VerifyBGPPeersHealth,
        "eos_data": [{"vrfs": {}}, {"vrfs": {}}, {"vrfs": {}}, {"vrfs": {}}],
        "inputs": {
            "address_families": [
                {"afi": "ipv4", "safi": "unicast", "vrf": "DEV"},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "MGMT"},
                {"afi": "link-state"},
                {"afi": "path-selection"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv4', 'safi': 'unicast', 'vrfs': {'DEV': 'Not Configured'}}, "
                "{'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'MGMT': 'Not Configured'}}, "
                "{'afi': 'link-state', 'vrfs': {'default': 'Not Configured'}}, "
                "{'afi': 'path-selection', 'vrfs': {'default': 'Not Configured'}}]"
            ],
        },
    },
    {
        "name": "failure-no-peers",
        "test": VerifyBGPPeersHealth,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "vrf": "default",
                        "routerId": "10.1.0.3",
                        "asn": "65120",
                        "peers": {},
                    }
                }
            },
            {
                "vrfs": {
                    "MGMT": {
                        "vrf": "MGMT",
                        "routerId": "10.1.0.3",
                        "asn": "65120",
                        "peers": {},
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "vrf": "default",
                        "routerId": "10.1.0.3",
                        "asn": "65120",
                        "peers": {},
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "vrf": "default",
                        "routerId": "10.1.0.3",
                        "asn": "65120",
                        "peers": {},
                    }
                }
            },
        ],
        "inputs": {
            "address_families": [
                {"afi": "ipv4", "safi": "multicast"},
                {"afi": "ipv4", "safi": "sr-te", "vrf": "MGMT"},
                {"afi": "link-state"},
                {"afi": "path-selection"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv4', 'safi': 'multicast', 'vrfs': {'default': 'No Peers'}}, {'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'MGMT': 'No Peers'}}, "
                "{'afi': 'link-state', 'vrfs': {'default': 'No Peers'}}, {'afi': 'path-selection', 'vrfs': {'default': 'No Peers'}}]"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPSpecificPeers,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.0": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.2": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peers": {
                            "10.1.255.10": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.12": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.20": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.22": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.30": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.32": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
        ],
        "inputs": {
            "address_families": [
                # Path selection first to make sure input to output mapping is correct.
                {"afi": "path-selection", "peers": ["10.1.255.20", "10.1.255.22"]},
                {
                    "afi": "ipv4",
                    "safi": "unicast",
                    "vrf": "default",
                    "peers": ["10.1.255.0", "10.1.255.2"],
                },
                {
                    "afi": "ipv4",
                    "safi": "sr-te",
                    "vrf": "MGMT",
                    "peers": ["10.1.255.10", "10.1.255.12"],
                },
                {"afi": "link-state", "peers": ["10.1.255.30", "10.1.255.32"]},
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-issues",
        "test": VerifyBGPSpecificPeers,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.0": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Idle",
                            },
                            "10.1.255.2": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peers": {
                            "10.1.255.10": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.12": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Idle",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.20": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Idle",
                            },
                            "10.1.255.22": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "peers": {
                            "10.1.255.30": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Established",
                            },
                            "10.1.255.32": {
                                "inMsgQueue": 0,
                                "outMsgQueue": 0,
                                "peerState": "Idle",
                            },
                        },
                    }
                }
            },
        ],
        "inputs": {
            "address_families": [
                {
                    "afi": "ipv4",
                    "safi": "unicast",
                    "vrf": "default",
                    "peers": ["10.1.255.0", "10.1.255.2"],
                },
                {
                    "afi": "ipv4",
                    "safi": "sr-te",
                    "vrf": "MGMT",
                    "peers": ["10.1.255.10", "10.1.255.12"],
                },
                {"afi": "path-selection", "peers": ["10.1.255.20", "10.1.255.22"]},
                {"afi": "link-state", "peers": ["10.1.255.30", "10.1.255.32"]},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv4', 'safi': 'unicast', 'vrfs': {'default': {'10.1.255.0': {'peerState': 'Idle', 'inMsgQueue': 0, 'outMsgQueue': 0}}}}, "
                "{'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'MGMT': {'10.1.255.12': {'peerState': 'Idle', 'inMsgQueue': 0, 'outMsgQueue': 0}}}}, "
                "{'afi': 'path-selection', 'vrfs': {'default': {'10.1.255.20': {'peerState': 'Idle', 'inMsgQueue': 0, 'outMsgQueue': 0}}}}, "
                "{'afi': 'link-state', 'vrfs': {'default': {'10.1.255.32': {'peerState': 'Idle', 'inMsgQueue': 0, 'outMsgQueue': 0}}}}]"
            ],
        },
    },
    {
        "name": "failure-not-configured",
        "test": VerifyBGPSpecificPeers,
        "eos_data": [{"vrfs": {}}, {"vrfs": {}}, {"vrfs": {}}, {"vrfs": {}}],
        "inputs": {
            "address_families": [
                {
                    "afi": "ipv4",
                    "safi": "unicast",
                    "vrf": "DEV",
                    "peers": ["10.1.255.0"],
                },
                {
                    "afi": "ipv4",
                    "safi": "sr-te",
                    "vrf": "MGMT",
                    "peers": ["10.1.255.10"],
                },
                {"afi": "link-state", "peers": ["10.1.255.20"]},
                {"afi": "path-selection", "peers": ["10.1.255.30"]},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv4', 'safi': 'unicast', 'vrfs': {'DEV': 'Not Configured'}}, "
                "{'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'MGMT': 'Not Configured'}}, {'afi': 'link-state', 'vrfs': {'default': 'Not Configured'}}, "
                "{'afi': 'path-selection', 'vrfs': {'default': 'Not Configured'}}]"
            ],
        },
    },
    {
        "name": "failure-no-peers",
        "test": VerifyBGPSpecificPeers,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "vrf": "default",
                        "routerId": "10.1.0.3",
                        "asn": "65120",
                        "peers": {},
                    }
                }
            },
            {
                "vrfs": {
                    "MGMT": {
                        "vrf": "MGMT",
                        "routerId": "10.1.0.3",
                        "asn": "65120",
                        "peers": {},
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "vrf": "default",
                        "routerId": "10.1.0.3",
                        "asn": "65120",
                        "peers": {},
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "vrf": "default",
                        "routerId": "10.1.0.3",
                        "asn": "65120",
                        "peers": {},
                    }
                }
            },
        ],
        "inputs": {
            "address_families": [
                {"afi": "ipv4", "safi": "multicast", "peers": ["10.1.255.0"]},
                {
                    "afi": "ipv4",
                    "safi": "sr-te",
                    "vrf": "MGMT",
                    "peers": ["10.1.255.10"],
                },
                {"afi": "link-state", "peers": ["10.1.255.20"]},
                {"afi": "path-selection", "peers": ["10.1.255.30"]},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Failures: [{'afi': 'ipv4', 'safi': 'multicast', 'vrfs': {'default': {'10.1.255.0': {'peerNotFound': True}}}}, "
                "{'afi': 'ipv4', 'safi': 'sr-te', 'vrfs': {'MGMT': {'10.1.255.10': {'peerNotFound': True}}}}, "
                "{'afi': 'link-state', 'vrfs': {'default': {'10.1.255.20': {'peerNotFound': True}}}}, "
                "{'afi': 'path-selection', 'vrfs': {'default': {'10.1.255.30': {'peerNotFound': True}}}}]"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPExchangedRoutes,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                            "192.0.254.5/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                            "192.0.254.5/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ],
                            },
                            "192.0.255.4/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ],
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ],
                            },
                            "192.0.255.4/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ],
                            },
                        },
                    }
                }
            },
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                    "advertised_routes": ["192.0.254.5/32", "192.0.254.3/32"],
                    "received_routes": ["192.0.254.3/32", "192.0.255.4/32"],
                },
                {
                    "peer_address": "172.30.11.5",
                    "vrf": "default",
                    "advertised_routes": ["192.0.254.3/32", "192.0.254.5/32"],
                    "received_routes": ["192.0.254.3/32", "192.0.255.4/32"],
                },
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-no-routes",
        "test": VerifyBGPExchangedRoutes,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "vrf": "default",
                        "routerId": "192.0.255.1",
                        "asn": "65001",
                        "bgpRouteEntries": {},
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "vrf": "default",
                        "routerId": "192.0.255.1",
                        "asn": "65001",
                        "bgpRouteEntries": {},
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "vrf": "default",
                        "routerId": "192.0.255.1",
                        "asn": "65001",
                        "bgpRouteEntries": {},
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "vrf": "default",
                        "routerId": "192.0.255.1",
                        "asn": "65001",
                        "bgpRouteEntries": {},
                    }
                }
            },
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.11",
                    "vrf": "default",
                    "advertised_routes": ["192.0.254.3/32"],
                    "received_routes": ["192.0.255.3/32"],
                },
                {
                    "peer_address": "172.30.11.12",
                    "vrf": "default",
                    "advertised_routes": ["192.0.254.31/32"],
                    "received_routes": ["192.0.255.31/32"],
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not found or routes are not exchanged properly:\n"
                "{'bgp_peers': {'172.30.11.11': {'default': 'Not configured'}, '172.30.11.12': {'default': 'Not configured'}}}"
            ],
        },
    },
    {
        "name": "failure-no-peer",
        "test": VerifyBGPExchangedRoutes,
        "eos_data": [
            {"vrfs": {}},
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                            "192.0.254.5/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                        },
                    }
                }
            },
            {"vrfs": {}},
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ],
                            },
                            "192.0.255.4/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ],
                            },
                        },
                    }
                }
            },
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.11",
                    "vrf": "MGMT",
                    "advertised_routes": ["192.0.254.3/32"],
                    "received_routes": ["192.0.255.3/32"],
                },
                {
                    "peer_address": "172.30.11.5",
                    "vrf": "default",
                    "advertised_routes": ["192.0.254.3/32", "192.0.254.5/32"],
                    "received_routes": ["192.0.254.3/32", "192.0.255.4/32"],
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": ["Following BGP peers are not found or routes are not exchanged properly:\n{'bgp_peers': {'172.30.11.11': {'MGMT': 'Not configured'}}}"],
        },
    },
    {
        "name": "failure-missing-routes",
        "test": VerifyBGPExchangedRoutes,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                            "192.0.254.5/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                            "192.0.254.5/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ],
                            },
                            "192.0.255.4/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ],
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ],
                            },
                            "192.0.255.4/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": True,
                                        },
                                    }
                                ],
                            },
                        },
                    }
                }
            },
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                    "advertised_routes": ["192.0.254.3/32", "192.0.254.51/32"],
                    "received_routes": ["192.0.254.31/32", "192.0.255.4/32"],
                },
                {
                    "peer_address": "172.30.11.5",
                    "vrf": "default",
                    "advertised_routes": ["192.0.254.31/32", "192.0.254.5/32"],
                    "received_routes": ["192.0.254.3/32", "192.0.255.41/32"],
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not found or routes are not exchanged properly:\n{'bgp_peers': "
                "{'172.30.11.1': {'default': {'advertised_routes': {'192.0.254.51/32': 'Not found'}, 'received_routes': {'192.0.254.31/32': 'Not found'}}}, "
                "'172.30.11.5': {'default': {'advertised_routes': {'192.0.254.31/32': 'Not found'}, 'received_routes': {'192.0.255.41/32': 'Not found'}}}}}"
            ],
        },
    },
    {
        "name": "failure-invalid-or-inactive-routes",
        "test": VerifyBGPExchangedRoutes,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": False,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                            "192.0.254.5/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": False,
                                        },
                                    }
                                ]
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": False,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                            "192.0.254.5/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": False,
                                            "active": True,
                                        },
                                    }
                                ]
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": False,
                                            "active": False,
                                        },
                                    }
                                ],
                            },
                            "192.0.255.4/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": False,
                                            "active": False,
                                        },
                                    }
                                ],
                            },
                        },
                    }
                }
            },
            {
                "vrfs": {
                    "default": {
                        "bgpRouteEntries": {
                            "192.0.254.3/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": False,
                                        },
                                    }
                                ],
                            },
                            "192.0.255.4/32": {
                                "bgpRoutePaths": [
                                    {
                                        "routeType": {
                                            "valid": True,
                                            "active": False,
                                        },
                                    }
                                ],
                            },
                        },
                    }
                }
            },
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                    "advertised_routes": ["192.0.254.3/32", "192.0.254.51/32"],
                    "received_routes": ["192.0.254.31/32", "192.0.255.4/32"],
                },
                {
                    "peer_address": "172.30.11.5",
                    "vrf": "default",
                    "advertised_routes": ["192.0.254.31/32", "192.0.254.5/32"],
                    "received_routes": ["192.0.254.3/32", "192.0.255.41/32"],
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not found or routes are not exchanged properly:\n{'bgp_peers': "
                "{'172.30.11.1': {'default': {'advertised_routes': {'192.0.254.3/32': {'valid': True, 'active': False}, '192.0.254.51/32': 'Not found'}, "
                "'received_routes': {'192.0.254.31/32': 'Not found', '192.0.255.4/32': {'valid': False, 'active': False}}}}, "
                "'172.30.11.5': {'default': {'advertised_routes': {'192.0.254.31/32': 'Not found', '192.0.254.5/32': {'valid': True, 'active': False}}, "
                "'received_routes': {'192.0.254.3/32': {'valid': False, 'active': True}, '192.0.255.41/32': 'Not found'}}}}}"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPPeerMPCaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                        "ipv4MplsLabels": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                    }
                                },
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                        "ipv4MplsVpn": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                    }
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                    "capabilities": ["Ipv4 Unicast", "ipv4 Mpls labels"],
                },
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "MGMT",
                    "capabilities": ["ipv4 Unicast", "ipv4 MplsVpn"],
                },
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-no-vrf",
        "test": VerifyBGPPeerMPCaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                        "ipv4MplsVpn": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                    }
                                },
                            }
                        ]
                    }
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "MGMT",
                    "capabilities": ["ipv4 Unicast", "ipv4mplslabels"],
                }
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer multiprotocol capabilities are not found or not ok:\n{'bgp_peers': {'172.30.11.1': {'MGMT': {'status': 'Not configured'}}}}"
            ],
        },
    },
    {
        "name": "failure-no-peer",
        "test": VerifyBGPPeerMPCaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        }
                                    },
                                },
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        }
                                    },
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "default",
                    "capabilities": ["ipv4Unicast", "L2 Vpn EVPN"],
                },
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "MGMT",
                    "capabilities": ["ipv4Unicast", "L2 Vpn EVPN"],
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer multiprotocol capabilities are not found or not ok:\n"
                "{'bgp_peers': {'172.30.11.10': {'default': {'status': 'Not configured'}}, '172.30.11.1': {'MGMT': {'status': 'Not configured'}}}}"
            ],
        },
    },
    {
        "name": "failure-missing-capabilities",
        "test": VerifyBGPPeerMPCaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        }
                                    },
                                },
                            }
                        ]
                    }
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                    "capabilities": ["ipv4 Unicast", "L2VpnEVPN"],
                }
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer multiprotocol capabilities are not found or not ok:\n{'bgp_peers': {'172.30.11.1': {'default': {'l2VpnEvpn': 'not found'}}}}"
            ],
        },
    },
    {
        "name": "failure-incorrect-capabilities",
        "test": VerifyBGPPeerMPCaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": False,
                                            "received": False,
                                            "enabled": False,
                                        },
                                        "ipv4MplsVpn": {
                                            "advertised": False,
                                            "received": True,
                                            "enabled": False,
                                        },
                                    },
                                },
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "l2VpnEvpn": {
                                            "advertised": True,
                                            "received": False,
                                            "enabled": False,
                                        },
                                        "ipv4MplsVpn": {
                                            "advertised": False,
                                            "received": False,
                                            "enabled": True,
                                        },
                                    },
                                },
                            },
                            {
                                "peerAddress": "172.30.11.11",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": False,
                                            "received": False,
                                            "enabled": False,
                                        },
                                        "ipv4MplsVpn": {
                                            "advertised": False,
                                            "received": False,
                                            "enabled": False,
                                        },
                                    },
                                },
                            },
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                    "capabilities": ["ipv4 unicast", "ipv4 mpls vpn", "L2 vpn EVPN"],
                },
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "MGMT",
                    "capabilities": ["ipv4unicast", "ipv4 mplsvpn", "L2vpnEVPN"],
                },
                {
                    "peer_address": "172.30.11.11",
                    "vrf": "MGMT",
                    "capabilities": ["Ipv4 Unicast", "ipv4 MPLSVPN", "L2 vpnEVPN"],
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer multiprotocol capabilities are not found or not ok:\n"
                "{'bgp_peers': {'172.30.11.1': {'default': {'ipv4Unicast': {'advertised': False, 'received': False, 'enabled': False}, "
                "'ipv4MplsVpn': {'advertised': False, 'received': True, 'enabled': False}, 'l2VpnEvpn': 'not found'}}, "
                "'172.30.11.10': {'MGMT': {'ipv4Unicast': 'not found', 'ipv4MplsVpn': {'advertised': False, 'received': False, 'enabled': True}, "
                "'l2VpnEvpn': {'advertised': True, 'received': False, 'enabled': False}}}, "
                "'172.30.11.11': {'MGMT': {'ipv4Unicast': {'advertised': False, 'received': False, 'enabled': False}, "
                "'ipv4MplsVpn': {'advertised': False, 'received': False, 'enabled': False}, 'l2VpnEvpn': 'not found'}}}}"
            ],
        },
    },
    {
        "name": "success-strict",
        "test": VerifyBGPPeerMPCaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                        "ipv4MplsLabels": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                    }
                                },
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                        "ipv4MplsVpn": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                    }
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                    "strict": True,
                    "capabilities": ["Ipv4 Unicast", "ipv4 Mpls labels"],
                },
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "MGMT",
                    "strict": True,
                    "capabilities": ["ipv4 Unicast", "ipv4 MplsVpn"],
                },
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-srict",
        "test": VerifyBGPPeerMPCaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                        "ipv4MplsLabels": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                    }
                                },
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        },
                                        "ipv4MplsVpn": {
                                            "advertised": False,
                                            "received": True,
                                            "enabled": True,
                                        },
                                    }
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                    "strict": True,
                    "capabilities": ["Ipv4 Unicast"],
                },
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "MGMT",
                    "strict": True,
                    "capabilities": ["ipv4MplsVpn", "L2vpnEVPN"],
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer multiprotocol capabilities are not found or not ok:\n{'bgp_peers': {'172.30.11.1': "
                "{'default': {'status': 'Expected only `ipv4Unicast` capabilities should be listed but found `ipv4Unicast, ipv4MplsLabels` instead.'}},"
                " '172.30.11.10': {'MGMT': {'status': 'Expected only `ipv4MplsVpn, l2VpnEvpn` capabilities should be listed but found `ipv4Unicast, "
                "ipv4MplsVpn` instead.'}}}}"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPPeerASNCap,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "fourOctetAsnCap": {
                                        "advertised": True,
                                        "received": True,
                                        "enabled": True,
                                    },
                                },
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "neighborCapabilities": {
                                    "fourOctetAsnCap": {
                                        "advertised": True,
                                        "received": True,
                                        "enabled": True,
                                    },
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                },
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "MGMT",
                },
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-no-vrf",
        "test": VerifyBGPPeerASNCap,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "fourOctetAsnCap": {
                                        "advertised": True,
                                        "received": True,
                                        "enabled": True,
                                    },
                                },
                            }
                        ]
                    }
                },
                "MGMT": {
                    "peerList": [
                        {
                            "peerAddress": "172.30.11.10",
                            "neighborCapabilities": {
                                "fourOctetAsnCap": {
                                    "advertised": True,
                                    "received": True,
                                    "enabled": True,
                                },
                            },
                        }
                    ]
                },
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "MGMT",
                },
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "default",
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer four octet asn capabilities are not found or not ok:\n"
                "{'bgp_peers': {'172.30.11.1': {'MGMT': {'status': 'Not configured'}}, '172.30.11.10': {'default': {'status': 'Not configured'}}}}"
            ],
        },
    },
    {
        "name": "failure-no-peer",
        "test": VerifyBGPPeerASNCap,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        }
                                    },
                                },
                            },
                        ]
                    }
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "default",
                }
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer four octet asn capabilities are not found or not ok:\n{'bgp_peers': {'172.30.11.10': {'default': {'status': 'Not configured'}}}}"
            ],
        },
    },
    {
        "name": "failure-missing-capabilities",
        "test": VerifyBGPPeerASNCap,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        }
                                    },
                                },
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4MplsLabels": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        }
                                    },
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "172.30.11.1", "vrf": "default"},
                {"peer_address": "172.30.11.10", "vrf": "MGMT"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer four octet asn capabilities are not found or not ok:\n"
                "{'bgp_peers': {'172.30.11.1': {'default': {'fourOctetAsnCap': 'not found'}}, '172.30.11.10': {'MGMT': {'fourOctetAsnCap': 'not found'}}}}"
            ],
        },
    },
    {
        "name": "failure-incorrect-capabilities",
        "test": VerifyBGPPeerASNCap,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "fourOctetAsnCap": {
                                        "advertised": False,
                                        "received": False,
                                        "enabled": False,
                                    },
                                },
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "neighborCapabilities": {
                                    "fourOctetAsnCap": {
                                        "advertised": True,
                                        "received": False,
                                        "enabled": True,
                                    },
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "172.30.11.1", "vrf": "default"},
                {"peer_address": "172.30.11.10", "vrf": "MGMT"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer four octet asn capabilities are not found or not ok:\n"
                "{'bgp_peers': {'172.30.11.1': {'default': {'fourOctetAsnCap': {'advertised': False, 'received': False, 'enabled': False}}}, "
                "'172.30.11.10': {'MGMT': {'fourOctetAsnCap': {'advertised': True, 'received': False, 'enabled': True}}}}}"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPPeerRouteRefreshCap,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "routeRefreshCap": {
                                        "advertised": True,
                                        "received": True,
                                        "enabled": True,
                                    },
                                },
                            }
                        ]
                    },
                    "CS": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.11",
                                "neighborCapabilities": {
                                    "routeRefreshCap": {
                                        "advertised": True,
                                        "received": True,
                                        "enabled": True,
                                    },
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                },
                {
                    "peer_address": "172.30.11.11",
                    "vrf": "CS",
                },
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-no-vrf",
        "test": VerifyBGPPeerRouteRefreshCap,
        "eos_data": [{"vrfs": {}}],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "MGMT",
                }
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer route refresh capabilities are not found or not ok:\n{'bgp_peers': {'172.30.11.1': {'MGMT': {'status': 'Not configured'}}}}"
            ],
        },
    },
    {
        "name": "failure-no-peer",
        "test": VerifyBGPPeerRouteRefreshCap,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ip4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        }
                                    },
                                },
                            }
                        ]
                    },
                    "CS": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.12",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ip4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        }
                                    },
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.12",
                    "vrf": "default",
                },
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "CS",
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer route refresh capabilities are not found or not ok:\n"
                "{'bgp_peers': {'172.30.11.12': {'default': {'status': 'Not configured'}}, '172.30.11.1': {'CS': {'status': 'Not configured'}}}}"
            ],
        },
    },
    {
        "name": "failure-missing-capabilities",
        "test": VerifyBGPPeerRouteRefreshCap,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        }
                                    },
                                },
                            }
                        ]
                    },
                    "CS": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.11",
                                "neighborCapabilities": {
                                    "multiprotocolCaps": {
                                        "ipv4Unicast": {
                                            "advertised": True,
                                            "received": True,
                                            "enabled": True,
                                        }
                                    },
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "172.30.11.1", "vrf": "default"},
                {"peer_address": "172.30.11.11", "vrf": "CS"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer route refresh capabilities are not found or not ok:\n"
                "{'bgp_peers': {'172.30.11.1': {'default': {'routeRefreshCap': 'not found'}}, '172.30.11.11': {'CS': {'routeRefreshCap': 'not found'}}}}"
            ],
        },
    },
    {
        "name": "failure-incorrect-capabilities",
        "test": VerifyBGPPeerRouteRefreshCap,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "neighborCapabilities": {
                                    "routeRefreshCap": {
                                        "advertised": False,
                                        "received": False,
                                        "enabled": False,
                                    },
                                },
                            }
                        ]
                    },
                    "CS": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.11",
                                "neighborCapabilities": {
                                    "routeRefreshCap": {
                                        "advertised": True,
                                        "received": True,
                                        "enabled": True,
                                    },
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "172.30.11.1", "vrf": "default"},
                {"peer_address": "172.30.11.11", "vrf": "CS"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peer route refresh capabilities are not found or not ok:\n"
                "{'bgp_peers': {'172.30.11.1': {'default': {'routeRefreshCap': {'advertised': False, 'received': False, 'enabled': False}}}}}"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPPeerMD5Auth,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "state": "Established",
                                "md5AuthEnabled": True,
                            }
                        ]
                    },
                    "CS": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "state": "Established",
                                "md5AuthEnabled": True,
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                },
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "CS",
                },
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-no-vrf",
        "test": VerifyBGPPeerMD5Auth,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "state": "Established",
                                "md5AuthEnabled": True,
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "MGMT",
                }
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not configured, not established or MD5 authentication is not enabled:\n"
                "{'bgp_peers': {'172.30.11.1': {'MGMT': {'status': 'Not configured'}}}}"
            ],
        },
    },
    {
        "name": "failure-no-peer",
        "test": VerifyBGPPeerMD5Auth,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "state": "Established",
                                "md5AuthEnabled": True,
                            }
                        ]
                    },
                    "CS": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.11",
                                "state": "Established",
                                "md5AuthEnabled": True,
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "default",
                },
                {
                    "peer_address": "172.30.11.11",
                    "vrf": "default",
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not configured, not established or MD5 authentication is not enabled:\n"
                "{'bgp_peers': {'172.30.11.10': {'default': {'status': 'Not configured'}}, '172.30.11.11': {'default': {'status': 'Not configured'}}}}"
            ],
        },
    },
    {
        "name": "failure-not-established-peer",
        "test": VerifyBGPPeerMD5Auth,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "state": "Idle",
                                "md5AuthEnabled": True,
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "state": "Idle",
                                "md5AuthEnabled": False,
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                },
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "MGMT",
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not configured, not established or MD5 authentication is not enabled:\n"
                "{'bgp_peers': {'172.30.11.1': {'default': {'state': 'Idle', 'md5_auth_enabled': True}}, "
                "'172.30.11.10': {'MGMT': {'state': 'Idle', 'md5_auth_enabled': False}}}}"
            ],
        },
    },
    {
        "name": "failure-not-md5-peer",
        "test": VerifyBGPPeerMD5Auth,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "state": "Established",
                            },
                            {
                                "peerAddress": "172.30.11.10",
                                "state": "Established",
                                "md5AuthEnabled": False,
                            },
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.11",
                                "state": "Established",
                                "md5AuthEnabled": False,
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                },
                {
                    "peer_address": "172.30.11.11",
                    "vrf": "MGMT",
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not configured, not established or MD5 authentication is not enabled:\n"
                "{'bgp_peers': {'172.30.11.1': {'default': {'state': 'Established', 'md5_auth_enabled': None}}, "
                "'172.30.11.11': {'MGMT': {'state': 'Established', 'md5_auth_enabled': False}}}}"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                },
            }
        ],
        "inputs": {"vxlan_endpoints": [{"address": "192.168.20.102", "vni": 10020}]},
        "expected": {"result": "success"},
    },
    {
        "name": "success-multiple-endpoints",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                },
            },
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10010 aac1.ab5d.b41e": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "vxlan_endpoints": [
                {"address": "192.168.20.102", "vni": 10020},
                {"address": "aac1.ab5d.b41e", "vni": 10010},
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "success-multiple-routes-ip",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                    "RD: 10.1.0.6:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                },
            },
        ],
        "inputs": {"vxlan_endpoints": [{"address": "192.168.20.102", "vni": 10020}]},
        "expected": {"result": "success"},
    },
    {
        "name": "success-multiple-routes-mac",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                    "RD: 10.1.0.6:500 mac-ip 10020 aac1.ab4e.bec2": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                },
            },
        ],
        "inputs": {"vxlan_endpoints": [{"address": "aac1.ab4e.bec2", "vni": 10020}]},
        "expected": {"result": "success"},
    },
    {
        "name": "success-multiple-routes-multiple-paths-ip",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                    "ecmp": True,
                                    "ecmpContributor": True,
                                    "ecmpHead": True,
                                },
                            },
                            {
                                "routeType": {
                                    "active": False,
                                    "valid": True,
                                    "ecmp": True,
                                    "ecmpContributor": True,
                                    "ecmpHead": False,
                                },
                            },
                        ]
                    },
                    "RD: 10.1.0.6:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                },
            },
        ],
        "inputs": {"vxlan_endpoints": [{"address": "192.168.20.102", "vni": 10020}]},
        "expected": {"result": "success"},
    },
    {
        "name": "success-multiple-routes-multiple-paths-mac",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                    "ecmp": True,
                                    "ecmpContributor": True,
                                    "ecmpHead": True,
                                },
                            },
                            {
                                "routeType": {
                                    "active": False,
                                    "valid": True,
                                    "ecmp": True,
                                    "ecmpContributor": True,
                                    "ecmpHead": False,
                                },
                            },
                        ]
                    },
                    "RD: 10.1.0.6:500 mac-ip 10020 aac1.ab4e.bec2": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                },
            },
        ],
        "inputs": {"vxlan_endpoints": [{"address": "aac1.ab4e.bec2", "vni": 10020}]},
        "expected": {"result": "success"},
    },
    {
        "name": "failure-no-routes",
        "test": VerifyEVPNType2Route,
        "eos_data": [{"vrf": "default", "routerId": "10.1.0.3", "asn": 65120, "evpnRoutes": {}}],
        "inputs": {"vxlan_endpoints": [{"address": "192.168.20.102", "vni": 10020}]},
        "expected": {
            "result": "failure",
            "messages": ["The following VXLAN endpoint do not have any EVPN Type-2 route: [('192.168.20.102', 10020)]"],
        },
    },
    {
        "name": "failure-path-not-active",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": False,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                },
            },
        ],
        "inputs": {"vxlan_endpoints": [{"address": "192.168.20.102", "vni": 10020}]},
        "expected": {
            "result": "failure",
            "messages": [
                "The following EVPN Type-2 routes do not have at least one valid and active path: ['RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102']"
            ],
        },
    },
    {
        "name": "failure-multiple-routes-not-active",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": False,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                    "RD: 10.1.0.6:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": False,
                                    "valid": False,
                                },
                            },
                        ]
                    },
                },
            },
        ],
        "inputs": {"vxlan_endpoints": [{"address": "192.168.20.102", "vni": 10020}]},
        "expected": {
            "result": "failure",
            "messages": [
                "The following EVPN Type-2 routes do not have at least one valid and active path: "
                "['RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102', "
                "'RD: 10.1.0.6:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102']"
            ],
        },
    },
    {
        "name": "failure-multiple-routes-multiple-paths-not-active",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": True,
                                    "valid": True,
                                },
                            },
                            {
                                "routeType": {
                                    "active": False,
                                    "valid": True,
                                },
                            },
                        ]
                    },
                    "RD: 10.1.0.6:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": False,
                                    "valid": False,
                                },
                            },
                            {
                                "routeType": {
                                    "active": False,
                                    "valid": False,
                                },
                            },
                        ]
                    },
                },
            },
        ],
        "inputs": {"vxlan_endpoints": [{"address": "192.168.20.102", "vni": 10020}]},
        "expected": {
            "result": "failure",
            "messages": [
                "The following EVPN Type-2 routes do not have at least one valid and active path: ['RD: 10.1.0.6:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102']"
            ],
        },
    },
    {
        "name": "failure-multiple-endpoints",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": False,
                                    "valid": False,
                                },
                            },
                        ]
                    },
                },
            },
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10010 aac1.ab5d.b41e": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": False,
                                    "valid": False,
                                },
                            },
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "vxlan_endpoints": [
                {"address": "192.168.20.102", "vni": 10020},
                {"address": "aac1.ab5d.b41e", "vni": 10010},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following EVPN Type-2 routes do not have at least one valid and active path: "
                "['RD: 10.1.0.5:500 mac-ip 10020 aac1.ab4e.bec2 192.168.20.102', "
                "'RD: 10.1.0.5:500 mac-ip 10010 aac1.ab5d.b41e']"
            ],
        },
    },
    {
        "name": "failure-multiple-endpoints-one-no-routes",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {"vrf": "default", "routerId": "10.1.0.3", "asn": 65120, "evpnRoutes": {}},
            {
                "vrf": "default",
                "routerId": "10.1.0.3",
                "asn": 65120,
                "evpnRoutes": {
                    "RD: 10.1.0.5:500 mac-ip 10010 aac1.ab5d.b41e 192.168.10.101": {
                        "evpnRoutePaths": [
                            {
                                "routeType": {
                                    "active": False,
                                    "valid": False,
                                },
                            },
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "vxlan_endpoints": [
                {"address": "aac1.ab4e.bec2", "vni": 10020},
                {"address": "192.168.10.101", "vni": 10010},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following VXLAN endpoint do not have any EVPN Type-2 route: [('aa:c1:ab:4e:be:c2', 10020)]",
                "The following EVPN Type-2 routes do not have at least one valid and active path: "
                "['RD: 10.1.0.5:500 mac-ip 10010 aac1.ab5d.b41e 192.168.10.101']",
            ],
        },
    },
    {
        "name": "failure-multiple-endpoints-no-routes",
        "test": VerifyEVPNType2Route,
        "eos_data": [
            {"vrf": "default", "routerId": "10.1.0.3", "asn": 65120, "evpnRoutes": {}},
            {"vrf": "default", "routerId": "10.1.0.3", "asn": 65120, "evpnRoutes": {}},
        ],
        "inputs": {
            "vxlan_endpoints": [
                {"address": "aac1.ab4e.bec2", "vni": 10020},
                {"address": "192.168.10.101", "vni": 10010},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": ["The following VXLAN endpoint do not have any EVPN Type-2 route: [('aa:c1:ab:4e:be:c2', 10020), ('192.168.10.101', 10010)]"],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPAdvCommunities,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "advertisedCommunities": {
                                    "standard": True,
                                    "extended": True,
                                    "large": True,
                                },
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "advertisedCommunities": {
                                    "standard": True,
                                    "extended": True,
                                    "large": True,
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                },
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "MGMT",
                },
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-no-vrf",
        "test": VerifyBGPAdvCommunities,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "advertisedCommunities": {
                                    "standard": True,
                                    "extended": True,
                                    "large": True,
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.17",
                    "vrf": "MGMT",
                }
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not configured or advertised communities are not standard, extended, and large:\n"
                "{'bgp_peers': {'172.30.11.17': {'MGMT': {'status': 'Not configured'}}}}"
            ],
        },
    },
    {
        "name": "failure-no-peer",
        "test": VerifyBGPAdvCommunities,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "advertisedCommunities": {
                                    "standard": True,
                                    "extended": True,
                                    "large": True,
                                },
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "advertisedCommunities": {
                                    "standard": True,
                                    "extended": True,
                                    "large": True,
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "default",
                },
                {
                    "peer_address": "172.30.11.12",
                    "vrf": "MGMT",
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not configured or advertised communities are not standard, extended, and large:\n"
                "{'bgp_peers': {'172.30.11.10': {'default': {'status': 'Not configured'}}, '172.30.11.12': {'MGMT': {'status': 'Not configured'}}}}"
            ],
        },
    },
    {
        "name": "failure-not-correct-communities",
        "test": VerifyBGPAdvCommunities,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "advertisedCommunities": {
                                    "standard": False,
                                    "extended": False,
                                    "large": False,
                                },
                            }
                        ]
                    },
                    "CS": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.10",
                                "advertisedCommunities": {
                                    "standard": True,
                                    "extended": True,
                                    "large": False,
                                },
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                },
                {
                    "peer_address": "172.30.11.10",
                    "vrf": "CS",
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not configured or advertised communities are not standard, extended, and large:\n"
                "{'bgp_peers': {'172.30.11.1': {'default': {'advertised_communities': {'standard': False, 'extended': False, 'large': False}}}, "
                "'172.30.11.10': {'CS': {'advertised_communities': {'standard': True, 'extended': True, 'large': False}}}}}"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPTimers,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "holdTime": 180,
                                "keepaliveTime": 60,
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.11",
                                "holdTime": 180,
                                "keepaliveTime": 60,
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                    "hold_time": 180,
                    "keep_alive_time": 60,
                },
                {
                    "peer_address": "172.30.11.11",
                    "vrf": "MGMT",
                    "hold_time": 180,
                    "keep_alive_time": 60,
                },
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-no-peer",
        "test": VerifyBGPTimers,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "holdTime": 180,
                                "keepaliveTime": 60,
                            }
                        ]
                    },
                    "MGMT": {"peerList": []},
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "MGMT",
                    "hold_time": 180,
                    "keep_alive_time": 60,
                },
                {
                    "peer_address": "172.30.11.11",
                    "vrf": "MGMT",
                    "hold_time": 180,
                    "keep_alive_time": 60,
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not configured or hold and keep-alive timers are not correct:\n"
                "{'172.30.11.1': {'MGMT': 'Not configured'}, '172.30.11.11': {'MGMT': 'Not configured'}}"
            ],
        },
    },
    {
        "name": "failure-not-correct-timers",
        "test": VerifyBGPTimers,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.1",
                                "holdTime": 160,
                                "keepaliveTime": 60,
                            }
                        ]
                    },
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "172.30.11.11",
                                "holdTime": 120,
                                "keepaliveTime": 40,
                            }
                        ]
                    },
                }
            }
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "172.30.11.1",
                    "vrf": "default",
                    "hold_time": 180,
                    "keep_alive_time": 60,
                },
                {
                    "peer_address": "172.30.11.11",
                    "vrf": "MGMT",
                    "hold_time": 180,
                    "keep_alive_time": 60,
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "Following BGP peers are not configured or hold and keep-alive timers are not correct:\n"
                "{'172.30.11.1': {'default': {'hold_time': 160, 'keep_alive_time': 60}}, "
                "'172.30.11.11': {'MGMT': {'hold_time': 120, 'keep_alive_time': 40}}}"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPPeerDropStats,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "dropStats": {
                                    "inDropAsloop": 0,
                                    "inDropClusterIdLoop": 0,
                                    "inDropMalformedMpbgp": 0,
                                    "inDropOrigId": 0,
                                    "inDropNhLocal": 0,
                                    "inDropNhAfV6": 0,
                                    "prefixDroppedMartianV4": 0,
                                    "prefixDroppedMaxRouteLimitViolatedV4": 0,
                                    "prefixDroppedMartianV6": 0,
                                },
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                                "dropStats": {
                                    "inDropAsloop": 0,
                                    "inDropClusterIdLoop": 0,
                                    "inDropMalformedMpbgp": 0,
                                    "inDropOrigId": 0,
                                    "inDropNhLocal": 0,
                                    "inDropNhAfV6": 0,
                                    "prefixDroppedMartianV4": 0,
                                    "prefixDroppedMaxRouteLimitViolatedV4": 0,
                                    "prefixDroppedMartianV6": 0,
                                },
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "10.100.0.8",
                    "vrf": "default",
                    "drop_stats": ["prefixDroppedMartianV4", "prefixDroppedMaxRouteLimitViolatedV4", "prefixDroppedMartianV6"],
                },
                {"peer_address": "10.100.0.9", "vrf": "MGMT", "drop_stats": ["inDropClusterIdLoop", "inDropOrigId", "inDropNhLocal"]},
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-not-found",
        "test": VerifyBGPPeerDropStats,
        "eos_data": [
            {"vrfs": {}},
            {"vrfs": {}},
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "10.100.0.8",
                    "vrf": "default",
                    "drop_stats": ["prefixDroppedMartianV4", "prefixDroppedMaxRouteLimitViolatedV4", "prefixDroppedMartianV6"],
                },
                {"peer_address": "10.100.0.9", "vrf": "MGMT", "drop_stats": ["inDropClusterIdLoop", "inDropOrigId", "inDropNhLocal"]},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or have non-zero NLRI drop statistics counters:\n"
                "{'10.100.0.8': {'default': 'Not configured'}, '10.100.0.9': {'MGMT': 'Not configured'}}"
            ],
        },
    },
    {
        "name": "failure",
        "test": VerifyBGPPeerDropStats,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "dropStats": {
                                    "inDropAsloop": 0,
                                    "inDropClusterIdLoop": 0,
                                    "inDropMalformedMpbgp": 0,
                                    "inDropOrigId": 1,
                                    "inDropNhLocal": 1,
                                    "inDropNhAfV6": 0,
                                    "prefixDroppedMartianV4": 1,
                                    "prefixDroppedMaxRouteLimitViolatedV4": 1,
                                    "prefixDroppedMartianV6": 0,
                                },
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                                "dropStats": {
                                    "inDropAsloop": 0,
                                    "inDropClusterIdLoop": 0,
                                    "inDropMalformedMpbgp": 0,
                                    "inDropOrigId": 1,
                                    "inDropNhLocal": 1,
                                    "inDropNhAfV6": 0,
                                    "prefixDroppedMartianV4": 0,
                                    "prefixDroppedMaxRouteLimitViolatedV4": 0,
                                    "prefixDroppedMartianV6": 0,
                                },
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {
                    "peer_address": "10.100.0.8",
                    "vrf": "default",
                    "drop_stats": ["prefixDroppedMartianV4", "prefixDroppedMaxRouteLimitViolatedV4", "prefixDroppedMartianV6"],
                },
                {"peer_address": "10.100.0.9", "vrf": "MGMT", "drop_stats": ["inDropClusterIdLoop", "inDropOrigId", "inDropNhLocal"]},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or have non-zero NLRI drop statistics counters:\n"
                "{'10.100.0.8': {'default': {'prefixDroppedMartianV4': 1, 'prefixDroppedMaxRouteLimitViolatedV4': 1}}, "
                "'10.100.0.9': {'MGMT': {'inDropOrigId': 1, 'inDropNhLocal': 1}}}"
            ],
        },
    },
    {
        "name": "success-all-drop-stats",
        "test": VerifyBGPPeerDropStats,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "dropStats": {
                                    "inDropAsloop": 0,
                                    "inDropClusterIdLoop": 0,
                                    "inDropMalformedMpbgp": 0,
                                    "inDropOrigId": 0,
                                    "inDropNhLocal": 0,
                                    "inDropNhAfV6": 0,
                                    "prefixDroppedMartianV4": 0,
                                    "prefixDroppedMaxRouteLimitViolatedV4": 0,
                                    "prefixDroppedMartianV6": 0,
                                },
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                                "dropStats": {
                                    "inDropAsloop": 0,
                                    "inDropClusterIdLoop": 0,
                                    "inDropMalformedMpbgp": 0,
                                    "inDropOrigId": 0,
                                    "inDropNhLocal": 0,
                                    "inDropNhAfV6": 0,
                                    "prefixDroppedMartianV4": 0,
                                    "prefixDroppedMaxRouteLimitViolatedV4": 0,
                                    "prefixDroppedMartianV6": 0,
                                },
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default"},
                {"peer_address": "10.100.0.9", "vrf": "MGMT"},
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-all-drop-stats",
        "test": VerifyBGPPeerDropStats,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "dropStats": {
                                    "inDropAsloop": 3,
                                    "inDropClusterIdLoop": 0,
                                    "inDropMalformedMpbgp": 0,
                                    "inDropOrigId": 1,
                                    "inDropNhLocal": 1,
                                    "inDropNhAfV6": 0,
                                    "prefixDroppedMartianV4": 1,
                                    "prefixDroppedMaxRouteLimitViolatedV4": 1,
                                    "prefixDroppedMartianV6": 0,
                                },
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                                "dropStats": {
                                    "inDropAsloop": 2,
                                    "inDropClusterIdLoop": 0,
                                    "inDropMalformedMpbgp": 0,
                                    "inDropOrigId": 1,
                                    "inDropNhLocal": 1,
                                    "inDropNhAfV6": 0,
                                    "prefixDroppedMartianV4": 0,
                                    "prefixDroppedMaxRouteLimitViolatedV4": 0,
                                    "prefixDroppedMartianV6": 0,
                                },
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default"},
                {"peer_address": "10.100.0.9", "vrf": "MGMT"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or have non-zero NLRI drop statistics counters:\n"
                "{'10.100.0.8': {'default': {'inDropAsloop': 3, 'inDropOrigId': 1, 'inDropNhLocal': 1, "
                "'prefixDroppedMartianV4': 1, 'prefixDroppedMaxRouteLimitViolatedV4': 1}}, "
                "'10.100.0.9': {'MGMT': {'inDropAsloop': 2, 'inDropOrigId': 1, 'inDropNhLocal': 1}}}"
            ],
        },
    },
    {
        "name": "failure-drop-stat-not-found",
        "test": VerifyBGPPeerDropStats,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "dropStats": {
                                    "inDropAsloop": 3,
                                    "inDropClusterIdLoop": 0,
                                    "inDropMalformedMpbgp": 0,
                                    "inDropOrigId": 1,
                                    "inDropNhLocal": 1,
                                    "inDropNhAfV6": 0,
                                    "prefixDroppedMaxRouteLimitViolatedV4": 1,
                                    "prefixDroppedMartianV6": 0,
                                },
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "drop_stats": ["inDropAsloop", "inDropOrigId", "inDropNhLocal", "prefixDroppedMartianV4"]}
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or have non-zero NLRI drop statistics counters:\n"
                "{'10.100.0.8': {'default': {'inDropAsloop': 3, 'inDropOrigId': 1, 'inDropNhLocal': 1, 'prefixDroppedMartianV4': 'Not Found'}}}"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPPeerUpdateErrors,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "peerInUpdateErrors": {
                                    "inUpdErrWithdraw": 0,
                                    "inUpdErrIgnore": 0,
                                    "inUpdErrDisableAfiSafi": 0,
                                    "disabledAfiSafi": "None",
                                    "lastUpdErrTime": 0,
                                },
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                                "peerInUpdateErrors": {
                                    "inUpdErrWithdraw": 0,
                                    "inUpdErrIgnore": 0,
                                    "inUpdErrDisableAfiSafi": 0,
                                    "disabledAfiSafi": "None",
                                    "lastUpdErrTime": 0,
                                },
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "update_errors": ["inUpdErrWithdraw", "inUpdErrIgnore", "disabledAfiSafi"]},
                {"peer_address": "10.100.0.9", "vrf": "MGMT", "update_errors": ["inUpdErrWithdraw", "inUpdErrIgnore", "disabledAfiSafi"]},
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-not-found",
        "test": VerifyBGPPeerUpdateErrors,
        "eos_data": [
            {"vrfs": {}},
            {"vrfs": {}},
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "update_errors": ["inUpdErrWithdraw", "inUpdErrIgnore", "disabledAfiSafi"]},
                {"peer_address": "10.100.0.9", "vrf": "MGMT", "update_errors": ["inUpdErrWithdraw", "inUpdErrIgnore", "disabledAfiSafi"]},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or have non-zero update error counters:\n"
                "{'10.100.0.8': {'default': 'Not configured'}, '10.100.0.9': {'MGMT': 'Not configured'}}"
            ],
        },
    },
    {
        "name": "failure-errors",
        "test": VerifyBGPPeerUpdateErrors,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "peerInUpdateErrors": {
                                    "inUpdErrWithdraw": 0,
                                    "inUpdErrIgnore": 0,
                                    "inUpdErrDisableAfiSafi": 0,
                                    "disabledAfiSafi": "ipv4Unicast",
                                    "lastUpdErrTime": 0,
                                },
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                                "peerInUpdateErrors": {
                                    "inUpdErrWithdraw": 1,
                                    "inUpdErrIgnore": 0,
                                    "inUpdErrDisableAfiSafi": 0,
                                    "disabledAfiSafi": "None",
                                    "lastUpdErrTime": 0,
                                },
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "update_errors": ["inUpdErrWithdraw", "inUpdErrIgnore", "disabledAfiSafi"]},
                {"peer_address": "10.100.0.9", "vrf": "MGMT", "update_errors": ["inUpdErrWithdraw", "inUpdErrIgnore", "disabledAfiSafi"]},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or have non-zero update error counters:\n"
                "{'10.100.0.8': {'default': {'disabledAfiSafi': 'ipv4Unicast'}}, "
                "'10.100.0.9': {'MGMT': {'inUpdErrWithdraw': 1}}}"
            ],
        },
    },
    {
        "name": "success-all-error-counters",
        "test": VerifyBGPPeerUpdateErrors,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "peerInUpdateErrors": {
                                    "inUpdErrWithdraw": 0,
                                    "inUpdErrIgnore": 0,
                                    "inUpdErrDisableAfiSafi": 0,
                                    "disabledAfiSafi": "None",
                                    "lastUpdErrTime": 0,
                                },
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                                "peerInUpdateErrors": {
                                    "inUpdErrWithdraw": 0,
                                    "inUpdErrIgnore": 0,
                                    "inUpdErrDisableAfiSafi": 0,
                                    "disabledAfiSafi": "None",
                                    "lastUpdErrTime": 0,
                                },
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default"},
                {"peer_address": "10.100.0.9", "vrf": "MGMT"},
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-all-error-counters",
        "test": VerifyBGPPeerUpdateErrors,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "peerInUpdateErrors": {
                                    "inUpdErrWithdraw": 1,
                                    "inUpdErrIgnore": 0,
                                    "inUpdErrDisableAfiSafi": 0,
                                    "disabledAfiSafi": "ipv4Unicast",
                                    "lastUpdErrTime": 0,
                                },
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                                "peerInUpdateErrors": {
                                    "inUpdErrWithdraw": 1,
                                    "inUpdErrIgnore": 0,
                                    "inUpdErrDisableAfiSafi": 1,
                                    "disabledAfiSafi": "None",
                                    "lastUpdErrTime": 0,
                                },
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "update_errors": ["inUpdErrWithdraw", "inUpdErrIgnore", "disabledAfiSafi"]},
                {
                    "peer_address": "10.100.0.9",
                    "vrf": "MGMT",
                    "update_errors": ["inUpdErrWithdraw", "inUpdErrIgnore", "disabledAfiSafi", "inUpdErrDisableAfiSafi"],
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or have non-zero update error counters:\n"
                "{'10.100.0.8': {'default': {'inUpdErrWithdraw': 1, 'disabledAfiSafi': 'ipv4Unicast'}}, "
                "'10.100.0.9': {'MGMT': {'inUpdErrWithdraw': 1, 'inUpdErrDisableAfiSafi': 1}}}"
            ],
        },
    },
    {
        "name": "failure-all-not-found",
        "test": VerifyBGPPeerUpdateErrors,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "peerInUpdateErrors": {
                                    "inUpdErrIgnore": 0,
                                    "inUpdErrDisableAfiSafi": 0,
                                    "disabledAfiSafi": "ipv4Unicast",
                                    "lastUpdErrTime": 0,
                                },
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                                "peerInUpdateErrors": {
                                    "inUpdErrWithdraw": 1,
                                    "inUpdErrIgnore": 0,
                                    "disabledAfiSafi": "None",
                                    "lastUpdErrTime": 0,
                                },
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "update_errors": ["inUpdErrWithdraw", "inUpdErrIgnore", "disabledAfiSafi"]},
                {
                    "peer_address": "10.100.0.9",
                    "vrf": "MGMT",
                    "update_errors": ["inUpdErrWithdraw", "inUpdErrIgnore", "disabledAfiSafi", "inUpdErrDisableAfiSafi"],
                },
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or have non-zero update error counters:\n"
                "{'10.100.0.8': {'default': {'inUpdErrWithdraw': 'Not Found', 'disabledAfiSafi': 'ipv4Unicast'}}, "
                "'10.100.0.9': {'MGMT': {'inUpdErrWithdraw': 1, 'inUpdErrDisableAfiSafi': 'Not Found'}}}"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBgpRouteMaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "routeMapInbound": "RM-MLAG-PEER-IN",
                                "routeMapOutbound": "RM-MLAG-PEER-OUT",
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.10",
                                "routeMapInbound": "RM-MLAG-PEER-IN",
                                "routeMapOutbound": "RM-MLAG-PEER-OUT",
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "inbound_route_map": "RM-MLAG-PEER-IN", "outbound_route_map": "RM-MLAG-PEER-OUT"},
                {"peer_address": "10.100.0.10", "vrf": "MGMT", "inbound_route_map": "RM-MLAG-PEER-IN", "outbound_route_map": "RM-MLAG-PEER-OUT"},
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-incorrect-route-map",
        "test": VerifyBgpRouteMaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "routeMapInbound": "RM-MLAG-PEER",
                                "routeMapOutbound": "RM-MLAG-PEER",
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.10",
                                "routeMapInbound": "RM-MLAG-PEER",
                                "routeMapOutbound": "RM-MLAG-PEER",
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "inbound_route_map": "RM-MLAG-PEER-IN", "outbound_route_map": "RM-MLAG-PEER-OUT"},
                {"peer_address": "10.100.0.10", "vrf": "MGMT", "inbound_route_map": "RM-MLAG-PEER-IN", "outbound_route_map": "RM-MLAG-PEER-OUT"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or has an incorrect or missing route map in either the inbound or outbound direction:\n"
                "{'10.100.0.8': {'default': {'Inbound route-map': 'RM-MLAG-PEER', 'Outbound route-map': 'RM-MLAG-PEER'}}, "
                "'10.100.0.10': {'MGMT': {'Inbound route-map': 'RM-MLAG-PEER', 'Outbound route-map': 'RM-MLAG-PEER'}}}"
            ],
        },
    },
    {
        "name": "failure-incorrect-inbound-map",
        "test": VerifyBgpRouteMaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "routeMapInbound": "RM-MLAG-PEER",
                                "routeMapOutbound": "RM-MLAG-PEER",
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.10",
                                "routeMapInbound": "RM-MLAG-PEER",
                                "routeMapOutbound": "RM-MLAG-PEER",
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "inbound_route_map": "RM-MLAG-PEER-IN"},
                {"peer_address": "10.100.0.10", "vrf": "MGMT", "inbound_route_map": "RM-MLAG-PEER-IN"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or has an incorrect or missing route map in either the inbound or outbound direction:\n"
                "{'10.100.0.8': {'default': {'Inbound route-map': 'RM-MLAG-PEER'}}, '10.100.0.10': {'MGMT': {'Inbound route-map': 'RM-MLAG-PEER'}}}"
            ],
        },
    },
    {
        "name": "failure-route-maps-not-configured",
        "test": VerifyBgpRouteMaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.10",
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "inbound_route_map": "RM-MLAG-PEER-IN", "outbound_route_map": "RM-MLAG-PEER-OUT"},
                {"peer_address": "10.100.0.10", "vrf": "MGMT", "inbound_route_map": "RM-MLAG-PEER-IN", "outbound_route_map": "RM-MLAG-PEER-OUT"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or has an incorrect or missing route map in either the inbound or outbound direction:\n"
                "{'10.100.0.8': {'default': {'Inbound route-map': 'Not Configured', 'Outbound route-map': 'Not Configured'}}, "
                "'10.100.0.10': {'MGMT': {'Inbound route-map': 'Not Configured', 'Outbound route-map': 'Not Configured'}}}"
            ],
        },
    },
    {
        "name": "failure-peer-not-found",
        "test": VerifyBgpRouteMaps,
        "eos_data": [
            {
                "vrfs": {
                    "default": {"peerList": []},
                },
            },
            {
                "vrfs": {
                    "MGMT": {"peerList": []},
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "inbound_route_map": "RM-MLAG-PEER-IN"},
                {"peer_address": "10.100.0.10", "vrf": "MGMT", "inbound_route_map": "RM-MLAG-PEER-IN"},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peers are not configured or has an incorrect or missing route map in either the inbound or outbound direction:\n"
                "{'10.100.0.8': {'default': 'Not configured'}, '10.100.0.10': {'MGMT': 'Not configured'}}"
            ],
        },
    },
    {
        "name": "success",
        "test": VerifyBGPPeerRouteLimit,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "maxTotalRoutes": 12000,
                                "totalRoutesWarnLimit": 10000,
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                                "maxTotalRoutes": 10000,
                                "totalRoutesWarnLimit": 9000,
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "maximum_routes": 12000, "warning_limit": 10000},
                {"peer_address": "10.100.0.9", "vrf": "MGMT", "maximum_routes": 10000},
            ]
        },
        "expected": {"result": "success"},
    },
    {
        "name": "failure-peer-not-found",
        "test": VerifyBGPPeerRouteLimit,
        "eos_data": [
            {
                "vrfs": {
                    "default": {},
                },
            },
            {
                "vrfs": {
                    "MGMT": {},
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "maximum_routes": 12000, "warning_limit": 10000},
                {"peer_address": "10.100.0.9", "vrf": "MGMT", "maximum_routes": 10000, "warning_limit": 9000},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peer(s) are not configured or maximum routes and maximum routes warning limit is not correct:\n"
                "{'10.100.0.8': {'default': 'Not configured'}, '10.100.0.9': {'MGMT': 'Not configured'}}"
            ],
        },
    },
    {
        "name": "failure-incorrect-max-routes",
        "test": VerifyBGPPeerRouteLimit,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "maxTotalRoutes": 13000,
                                "totalRoutesWarnLimit": 11000,
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                                "maxTotalRoutes": 11000,
                                "totalRoutesWarnLimit": 10000,
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "maximum_routes": 12000, "warning_limit": 10000},
                {"peer_address": "10.100.0.9", "vrf": "MGMT", "maximum_routes": 10000, "warning_limit": 9000},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peer(s) are not configured or maximum routes and maximum routes warning limit is not correct:\n"
                "{'10.100.0.8': {'default': {'Maximum total routes': 13000, 'Warning limit': 11000}}, "
                "'10.100.0.9': {'MGMT': {'Maximum total routes': 11000, 'Warning limit': 10000}}}"
            ],
        },
    },
    {
        "name": "failure-routes-not-found",
        "test": VerifyBGPPeerRouteLimit,
        "eos_data": [
            {
                "vrfs": {
                    "default": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.8",
                                "maxTotalRoutes": 12000,
                            }
                        ]
                    },
                },
            },
            {
                "vrfs": {
                    "MGMT": {
                        "peerList": [
                            {
                                "peerAddress": "10.100.0.9",
                            }
                        ]
                    },
                },
            },
        ],
        "inputs": {
            "bgp_peers": [
                {"peer_address": "10.100.0.8", "vrf": "default", "maximum_routes": 12000, "warning_limit": 10000},
                {"peer_address": "10.100.0.9", "vrf": "MGMT", "maximum_routes": 10000, "warning_limit": 9000},
            ]
        },
        "expected": {
            "result": "failure",
            "messages": [
                "The following BGP peer(s) are not configured or maximum routes and maximum routes warning limit is not correct:\n"
                "{'10.100.0.8': {'default': {'Warning limit': 'Not Found'}}, "
                "'10.100.0.9': {'MGMT': {'Maximum total routes': 'Not Found', 'Warning limit': 'Not Found'}}}"
            ],
        },
    },
]
