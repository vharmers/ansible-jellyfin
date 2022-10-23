
def test_installed(host):
    package = host.package("jellyfin")
    assert package.is_installed


def test_service(host):
    service = host.service("jellyfin")
    assert service.is_running
    assert service.is_enabled
