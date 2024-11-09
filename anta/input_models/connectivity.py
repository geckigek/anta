# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Module containing input models for connectivity tests."""

from __future__ import annotations

from ipaddress import IPv4Address

from pydantic import BaseModel, ConfigDict

from anta.custom_types import Interface


class Host(BaseModel):
    """Model for a remote host to ping."""

    model_config = ConfigDict(extra="forbid")
    destination: IPv4Address
    """IPv4 address to ping."""
    source: IPv4Address | Interface
    """IPv4 address source IP or egress interface to use."""
    vrf: str = "default"
    """VRF context. Defaults to `default`."""
    repeat: int = 2
    """Number of ping repetition. Defaults to 2."""
    size: int = 100
    """Specify datagram size. Defaults to 100."""
    df_bit: bool = False
    """Enable do not fragment bit in IP header. Defaults to False."""

    def __str__(self) -> str:
        """Return a human-readable string representation of the Host for reporting.

        Examples
        --------
        Host 10.1.1.1 (src: 10.2.2.2, vrf: mgmt, size: 100B, repeat: 2)

        """
        df_status = ", df-bit: enabled" if self.df_bit else ""
        return f"Host {self.destination} (src: {self.source}, vrf: {self.vrf}, size: {self.size}B, repeat: {self.repeat}{df_status})"
