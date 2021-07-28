using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;


namespace midi_controller_ui
{
    public partial class Form1 : Form
    {
        static int id = 31;
           
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            label2.Text = "Status: Enabled";
            openController();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label2.Text = "Status: Disabled";
            closeController();
        }

        private void label1_Click(object sender, EventArgs e)
        { 

        }

        private void openController()
        {
            var process = customProcess.Instance;
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            startInfo.FileName = "wt.exe";
            // for debug add 3x parent
            // for release only fullname and add controller.py to release folder
            string path = new DirectoryInfo(Environment.CurrentDirectory).FullName;
            startInfo.Arguments = "python " + path + "\\controller.py";
            try
            {
                process.StartInfo = startInfo;
                process.Start();
                id = process.getId();
            }
            catch (Exception ex)
            {
                label2.Text = "Cannot create another\n process while a process in running.";
            }
        }

        private void closeController()
        {
            customProcess process = customProcess.GetCustomProcessById(id);
            if (process != null)
                process.delInstance();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
