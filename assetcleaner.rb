class Assetcleaner < Formula
  include Language::Python::Virtualenv

  desc "Find and remove unused assets from Xcode projects"
  homepage "https://github.com/yourusername/asset-cleaner"
  url "https://github.com/yourusername/asset-cleaner/archive/v1.0.0.tar.gz"
  sha256 "YOUR_SHA256_HERE"
  license "MIT"

  depends_on "python@3.11"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/assetcleaner", "--help"
  end
end
