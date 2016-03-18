using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Runtime;
using System.Text;

namespace COMPILE
{
    class Program
    {
        static void Main(string[] args)
        {
            // First, see if we need to clean the output folder.
            if (Directory.Exists("./__pycache__/"))
            {
                Console.Write("Cleaning output directory . . . ");
                Directory.Delete("./__pycache__/", true);
                Console.WriteLine(" Done!\n");
            }

            // Compile the Python Code.
            Console.Write("Compiling Python Code . . . ");

            if (!Directory.Exists("C:\\Python34"))
            {
                Console.WriteLine("ERROR! Python 3.4 is not installed on this system. Aborting compilation.");
                Environment.Exit(1);
            }

            // Look in to optimizing the bytecode (-OO or -O)
            ProcessStartInfo processInfo = new ProcessStartInfo("C:\\Python34\\python.exe", "-m compileall .");
            processInfo.WorkingDirectory = ".\\";
            processInfo.UseShellExecute = true;

            Process myProcess = new Process();

            myProcess.StartInfo = processInfo;
            myProcess.Start();
            myProcess.WaitForExit();

            Console.WriteLine(" Done!\n");

            // Remove the cpython-34 garbage.
            Console.Write("Cleaning up object files . . . ");

            string[] compiledFiles = Directory.GetFiles(".\\__pycache__\\", "*.pyc");

            foreach (string file in compiledFiles)
            {
                string rename = file.Replace(".cpython-34", "");
                File.Move(file, rename);
            }

            Console.WriteLine(" Done!\n");

            // Copy the game assets.
            Console.Write("Copying Game Assets . . . ");

            DirectoryCopy("./Resources/", "./__pycache__/Resources/", true);

            Console.WriteLine(" Done!\n");
        }

        private static void DirectoryCopy(string sourceDirName, string destDirName, bool copySubDirs)
        {
            // Get the subdirectories for the specified directory.
            DirectoryInfo dir = new DirectoryInfo(sourceDirName);
            DirectoryInfo[] dirs = dir.GetDirectories();

            if (!dir.Exists)
            {
                throw new DirectoryNotFoundException(
                    "Source directory does not exist or could not be found: "
                    + sourceDirName);
            }

            // If the destination directory doesn't exist, create it. 
            if (!Directory.Exists(destDirName))
            {
                Directory.CreateDirectory(destDirName);
            }

            // Get the files in the directory and copy them to the new location.
            FileInfo[] files = dir.GetFiles();
            foreach (FileInfo file in files)
            {
                string temppath = Path.Combine(destDirName, file.Name);
                file.CopyTo(temppath, false);
            }

            // If copying subdirectories, copy them and their contents to new location. 
            if (copySubDirs)
            {
                foreach (DirectoryInfo subdir in dirs)
                {
                    string temppath = Path.Combine(destDirName, subdir.Name);
                    DirectoryCopy(subdir.FullName, temppath, copySubDirs);
                }
            }
        }
    }
}
