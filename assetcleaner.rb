class Assetcleaner < Formula
  include Language::Python::Virtualenv

  desc "Find and remove unused assets from Xcode projects"
  homepage "https://github.com/m00nbek/asset-cleaner"
  url "https://github.com/m00nbek/asset-cleaner/archive/v1.0.0.tar.gz"
  sha256 "dbd705a41f87706c4d5a572cc10c3bf36696f9980753887604aa0d862a13fb23"
  license "MIT"

  depends_on "python@3.11"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/assetcleaner", "--help"
  end
end
