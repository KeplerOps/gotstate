# tests/unit/test_concurrency.py
# Copyright (c) 2024 Brad Edwards
# Licensed under the MIT License - see LICENSE file for details

from unittest.mock import MagicMock


def test_lock_factory():
    from hsm.runtime.concurrency import _LockFactory

    lf = _LockFactory()
    lock = lf.create_lock()
    assert hasattr(lock, "acquire")
    assert hasattr(lock, "release")


def test_lock_context_manager():
    from hsm.runtime.concurrency import _LockContextManager

    lock = MagicMock()
    with _LockContextManager(lock):
        lock.acquire.assert_called_once()
    lock.release.assert_called_once()