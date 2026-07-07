using DevExpress.XtraEditors;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DVLD_System
{
    public partial class frmLoginScreen : DevExpress.XtraEditors.XtraForm
    {
        public frmLoginScreen()
        {
            InitializeComponent();
        }

        private void frmLoginScreen_Shown(object sender, EventArgs e)
        {
            ucLogin1.FocusUserName();
            ucLogin1.Select();
        }
    }
}