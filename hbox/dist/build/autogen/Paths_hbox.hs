module Paths_hbox (
    version,
    getBinDir, getLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
catchIO = Exception.catch


version :: Version
version = Version {versionBranch = [0,1,0,0], versionTags = []}
bindir, libdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/Users/asad/.cabal/bin"
libdir     = "/Users/asad/.cabal/lib/x86_64-osx-ghc-7.8.3/hbox-0.1.0.0"
datadir    = "/Users/asad/.cabal/share/x86_64-osx-ghc-7.8.3/hbox-0.1.0.0"
libexecdir = "/Users/asad/.cabal/libexec"
sysconfdir = "/Users/asad/.cabal/etc"

getBinDir, getLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "hbox_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "hbox_libdir") (\_ -> return libdir)
getDataDir = catchIO (getEnv "hbox_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "hbox_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "hbox_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
