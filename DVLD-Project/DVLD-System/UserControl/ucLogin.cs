using DevExpress.XtraEditors;
using DevExpress.XtraWaitForm;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.TextBox;

namespace DVLD_System
{
    public partial class ucLogin : DevExpress.XtraEditors.XtraUserControl
    {
        private CheckEdit chkRememberMe;
        private LabelControl lblLogin;
        private HyperlinkLabelControl lnkForgotPassword;
        private HyperlinkLabelControl lnkSignUp;
        private SimpleButton btnClose2;
        private Guna.UI2.WinForms.Guna2Panel pnlLogin;
        private LabelControl lblWelcome;
        private Guna.UI2.WinForms.Guna2PictureBox imgCar;
        private LabelControl lblVersion;
        private SimpleButton btnLogin;
        private Guna.UI2.WinForms.Guna2GroupBox grpLogin;
        private TextBox txtPassword;
        private DevExpress.XtraEditors.TextEdit txtUsername;
        private LabelControl lblPassword;
        private LabelControl lblUsername;
        private SimpleButton btnClose1;
        private Guna.UI2.WinForms.Guna2CirclePictureBox imgVisionOpen;
        private Guna.UI2.WinForms.Guna2CirclePictureBox imgVisionClose;
        private LabelControl lblCopyright;

        public ucLogin()
        {
            InitializeComponent();
            SetupPlaceholders();

        }

        private void SetupPlaceholders()
        {
            txtUsername.Properties.NullValuePrompt = "Enter username";
            txtUsername.Properties.NullValuePromptShowForEmptyValue = true;

        }

        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ucLogin));
            this.lblLogin = new DevExpress.XtraEditors.LabelControl();
            this.lnkForgotPassword = new DevExpress.XtraEditors.HyperlinkLabelControl();
            this.lnkSignUp = new DevExpress.XtraEditors.HyperlinkLabelControl();
            this.lblCopyright = new DevExpress.XtraEditors.LabelControl();
            this.btnClose2 = new DevExpress.XtraEditors.SimpleButton();
            this.pnlLogin = new Guna.UI2.WinForms.Guna2Panel();
            this.lblVersion = new DevExpress.XtraEditors.LabelControl();
            this.lblWelcome = new DevExpress.XtraEditors.LabelControl();
            this.btnLogin = new DevExpress.XtraEditors.SimpleButton();
            this.grpLogin = new Guna.UI2.WinForms.Guna2GroupBox();
            this.txtPassword = new System.Windows.Forms.TextBox();
            this.lblPassword = new DevExpress.XtraEditors.LabelControl();
            this.lblUsername = new DevExpress.XtraEditors.LabelControl();
            this.imgVisionClose = new Guna.UI2.WinForms.Guna2CirclePictureBox();
            this.imgVisionOpen = new Guna.UI2.WinForms.Guna2CirclePictureBox();
            this.btnClose1 = new DevExpress.XtraEditors.SimpleButton();
            this.txtUsername = new DevExpress.XtraEditors.TextEdit();
            this.chkRememberMe = new DevExpress.XtraEditors.CheckEdit();
            this.imgCar = new Guna.UI2.WinForms.Guna2PictureBox();
            this.pnlLogin.SuspendLayout();
            this.grpLogin.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.imgVisionClose)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.imgVisionOpen)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.txtUsername.Properties)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chkRememberMe.Properties)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.imgCar)).BeginInit();
            this.SuspendLayout();
            // 
            // lblLogin
            // 
            this.lblLogin.Appearance.Font = new System.Drawing.Font("Tahoma", 18F, System.Drawing.FontStyle.Bold);
            this.lblLogin.Appearance.Options.UseFont = true;
            this.lblLogin.Location = new System.Drawing.Point(16, 8);
            this.lblLogin.Name = "lblLogin";
            this.lblLogin.Size = new System.Drawing.Size(261, 29);
            this.lblLogin.TabIndex = 7;
            this.lblLogin.Text = "Login to your account";
            // 
            // lnkForgotPassword
            // 
            this.lnkForgotPassword.Appearance.Font = new System.Drawing.Font("Tahoma", 10F);
            this.lnkForgotPassword.Appearance.Options.UseFont = true;
            this.lnkForgotPassword.Location = new System.Drawing.Point(312, 176);
            this.lnkForgotPassword.Name = "lnkForgotPassword";
            this.lnkForgotPassword.Size = new System.Drawing.Size(96, 16);
            this.lnkForgotPassword.TabIndex = 6;
            this.lnkForgotPassword.Text = "Forgot Password";
            // 
            // lnkSignUp
            // 
            this.lnkSignUp.Location = new System.Drawing.Point(104, 368);
            this.lnkSignUp.Name = "lnkSignUp";
            this.lnkSignUp.Size = new System.Drawing.Size(36, 13);
            this.lnkSignUp.TabIndex = 15;
            this.lnkSignUp.Text = "Sign Up";
            // 
            // lblCopyright
            // 
            this.lblCopyright.Location = new System.Drawing.Point(56, 408);
            this.lblCopyright.Name = "lblCopyright";
            this.lblCopyright.Size = new System.Drawing.Size(130, 13);
            this.lblCopyright.TabIndex = 16;
            this.lblCopyright.Text = "Copyright © 2026 by DVLD";
            // 
            // btnClose2
            // 
            this.btnClose2.Appearance.BackColor = System.Drawing.SystemColors.GradientInactiveCaption;
            this.btnClose2.Appearance.Font = new System.Drawing.Font("Tahoma", 16F);
            this.btnClose2.Appearance.Options.UseBackColor = true;
            this.btnClose2.Appearance.Options.UseFont = true;
            this.btnClose2.AppearanceHovered.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.btnClose2.AppearanceHovered.ForeColor = System.Drawing.Color.Blue;
            this.btnClose2.AppearanceHovered.Options.UseBorderColor = true;
            this.btnClose2.AppearanceHovered.Options.UseForeColor = true;
            this.btnClose2.Location = new System.Drawing.Point(232, 280);
            this.btnClose2.Name = "btnClose2";
            this.btnClose2.Size = new System.Drawing.Size(160, 40);
            this.btnClose2.TabIndex = 3;
            this.btnClose2.Text = "Close";
            this.btnClose2.Click += new System.EventHandler(this.btnClose2_Click);
            // 
            // pnlLogin
            // 
            this.pnlLogin.BackColor = System.Drawing.Color.Transparent;
            this.pnlLogin.Controls.Add(this.imgCar);
            this.pnlLogin.Controls.Add(this.lblVersion);
            this.pnlLogin.Controls.Add(this.lblWelcome);
            this.pnlLogin.Controls.Add(this.lblCopyright);
            this.pnlLogin.Controls.Add(this.lnkSignUp);
            this.pnlLogin.ForeColor = System.Drawing.Color.Blue;
            this.pnlLogin.Location = new System.Drawing.Point(8, 16);
            this.pnlLogin.Name = "pnlLogin";
            this.pnlLogin.Size = new System.Drawing.Size(264, 432);
            this.pnlLogin.TabIndex = 18;
            // 
            // lblVersion
            // 
            this.lblVersion.Appearance.Font = new System.Drawing.Font("Tahoma", 10F);
            this.lblVersion.Appearance.Options.UseFont = true;
            this.lblVersion.Location = new System.Drawing.Point(88, 328);
            this.lblVersion.Name = "lblVersion";
            this.lblVersion.Size = new System.Drawing.Size(65, 16);
            this.lblVersion.TabIndex = 14;
            this.lblVersion.Text = "Version 1.0";
            // 
            // lblWelcome
            // 
            this.lblWelcome.Appearance.Font = new System.Drawing.Font("Tahoma", 16F, System.Drawing.FontStyle.Bold);
            this.lblWelcome.Appearance.Options.UseFont = true;
            this.lblWelcome.Appearance.Options.UseTextOptions = true;
            this.lblWelcome.Appearance.TextOptions.HAlignment = DevExpress.Utils.HorzAlignment.Center;
            this.lblWelcome.Appearance.TextOptions.WordWrap = DevExpress.Utils.WordWrap.Wrap;
            this.lblWelcome.AppearanceDisabled.Options.UseTextOptions = true;
            this.lblWelcome.AppearanceDisabled.TextOptions.VAlignment = DevExpress.Utils.VertAlignment.Center;
            this.lblWelcome.AutoSizeMode = DevExpress.XtraEditors.LabelAutoSizeMode.None;
            this.lblWelcome.Location = new System.Drawing.Point(8, 192);
            this.lblWelcome.Name = "lblWelcome";
            this.lblWelcome.Size = new System.Drawing.Size(248, 128);
            this.lblWelcome.TabIndex = 13;
            this.lblWelcome.Text = "Welcome to \r\nDrivers & Vehicles License Department (DVLD) System ";
            this.lblWelcome.UseMnemonic = false;
            // 
            // btnLogin
            // 
            this.btnLogin.Appearance.BackColor = System.Drawing.SystemColors.GradientInactiveCaption;
            this.btnLogin.Appearance.Font = new System.Drawing.Font("Tahoma", 16F);
            this.btnLogin.Appearance.Options.UseBackColor = true;
            this.btnLogin.Appearance.Options.UseFont = true;
            this.btnLogin.AppearanceHovered.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.btnLogin.AppearanceHovered.ForeColor = System.Drawing.Color.Blue;
            this.btnLogin.AppearanceHovered.Options.UseBorderColor = true;
            this.btnLogin.AppearanceHovered.Options.UseForeColor = true;
            this.btnLogin.Location = new System.Drawing.Point(40, 280);
            this.btnLogin.Name = "btnLogin";
            this.btnLogin.Size = new System.Drawing.Size(160, 40);
            this.btnLogin.TabIndex = 2;
            this.btnLogin.Text = "Login";
            this.btnLogin.Click += new System.EventHandler(this.btnLogin_Click);
            // 
            // grpLogin
            // 
            this.grpLogin.Controls.Add(this.imgVisionClose);
            this.grpLogin.Controls.Add(this.imgVisionOpen);
            this.grpLogin.Controls.Add(this.btnClose1);
            this.grpLogin.Controls.Add(this.txtPassword);
            this.grpLogin.Controls.Add(this.txtUsername);
            this.grpLogin.Controls.Add(this.lblPassword);
            this.grpLogin.Controls.Add(this.lblLogin);
            this.grpLogin.Controls.Add(this.lblUsername);
            this.grpLogin.Controls.Add(this.btnLogin);
            this.grpLogin.Controls.Add(this.btnClose2);
            this.grpLogin.Controls.Add(this.chkRememberMe);
            this.grpLogin.Controls.Add(this.lnkForgotPassword);
            this.grpLogin.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.grpLogin.ForeColor = System.Drawing.Color.Black;
            this.grpLogin.Location = new System.Drawing.Point(280, 16);
            this.grpLogin.Name = "grpLogin";
            this.grpLogin.Size = new System.Drawing.Size(416, 432);
            this.grpLogin.TabIndex = 17;
            // 
            // txtPassword
            // 
            this.txtPassword.Font = new System.Drawing.Font("Tahoma", 16F);
            this.txtPassword.Location = new System.Drawing.Point(112, 128);
            this.txtPassword.MaxLength = 20;
            this.txtPassword.Name = "txtPassword";
            this.txtPassword.Size = new System.Drawing.Size(296, 33);
            this.txtPassword.TabIndex = 1;
            this.txtPassword.UseSystemPasswordChar = true;
            // 
            // lblPassword
            // 
            this.lblPassword.Appearance.Font = new System.Drawing.Font("Tahoma", 16F);
            this.lblPassword.Appearance.Options.UseFont = true;
            this.lblPassword.Location = new System.Drawing.Point(8, 128);
            this.lblPassword.Name = "lblPassword";
            this.lblPassword.Size = new System.Drawing.Size(95, 25);
            this.lblPassword.TabIndex = 20;
            this.lblPassword.Text = "Password ";
            // 
            // lblUsername
            // 
            this.lblUsername.Appearance.Font = new System.Drawing.Font("Tahoma", 16F);
            this.lblUsername.Appearance.Options.UseFont = true;
            this.lblUsername.Location = new System.Drawing.Point(8, 72);
            this.lblUsername.Name = "lblUsername";
            this.lblUsername.Size = new System.Drawing.Size(94, 25);
            this.lblUsername.TabIndex = 19;
            this.lblUsername.Text = "Username";
            // 
            // imgVisionClose
            // 
            this.imgVisionClose.BackColor = System.Drawing.Color.Transparent;
            this.imgVisionClose.Image = global::DVLD_System.Properties.Resources.picVisionClose;
            this.imgVisionClose.ImageRotate = 0F;
            this.imgVisionClose.Location = new System.Drawing.Point(368, 136);
            this.imgVisionClose.Name = "imgVisionClose";
            this.imgVisionClose.ShadowDecoration.Mode = Guna.UI2.WinForms.Enums.ShadowMode.Circle;
            this.imgVisionClose.Size = new System.Drawing.Size(32, 16);
            this.imgVisionClose.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.imgVisionClose.TabIndex = 21;
            this.imgVisionClose.TabStop = false;
            this.imgVisionClose.Click += new System.EventHandler(this.imgVisionClose_Click);
            // 
            // imgVisionOpen
            // 
            this.imgVisionOpen.BackColor = System.Drawing.Color.Transparent;
            this.imgVisionOpen.Image = global::DVLD_System.Properties.Resources.picVision;
            this.imgVisionOpen.ImageRotate = 0F;
            this.imgVisionOpen.Location = new System.Drawing.Point(368, 136);
            this.imgVisionOpen.Name = "imgVisionOpen";
            this.imgVisionOpen.ShadowDecoration.Mode = Guna.UI2.WinForms.Enums.ShadowMode.Circle;
            this.imgVisionOpen.Size = new System.Drawing.Size(32, 16);
            this.imgVisionOpen.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.imgVisionOpen.TabIndex = 20;
            this.imgVisionOpen.TabStop = false;
            this.imgVisionOpen.Click += new System.EventHandler(this.imgVisionOpen_Click);
            // 
            // btnClose1
            // 
            this.btnClose1.Appearance.Font = new System.Drawing.Font("Tahoma", 16F);
            this.btnClose1.Appearance.Options.UseFont = true;
            this.btnClose1.AppearanceHovered.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.btnClose1.AppearanceHovered.Options.UseBorderColor = true;
            this.btnClose1.ImageOptions.Image = ((System.Drawing.Image)(resources.GetObject("btnClose1.ImageOptions.Image")));
            this.btnClose1.Location = new System.Drawing.Point(376, 0);
            this.btnClose1.Name = "btnClose1";
            this.btnClose1.PaintStyle = DevExpress.XtraEditors.Controls.PaintStyles.Light;
            this.btnClose1.Size = new System.Drawing.Size(40, 40);
            this.btnClose1.TabIndex = 5;
            this.btnClose1.Click += new System.EventHandler(this.btnClose2_Click);
            // 
            // txtUsername
            // 
            this.txtUsername.Location = new System.Drawing.Point(112, 72);
            this.txtUsername.Name = "txtUsername";
            this.txtUsername.Properties.Appearance.Font = new System.Drawing.Font("Tahoma", 16F);
            this.txtUsername.Properties.Appearance.Options.UseFont = true;
            this.txtUsername.Properties.MaxLength = 20;
            this.txtUsername.Properties.UseMaskAsDisplayFormat = true;
            this.txtUsername.Size = new System.Drawing.Size(296, 32);
            this.txtUsername.TabIndex = 0;
            // 
            // chkRememberMe
            // 
            this.chkRememberMe.Location = new System.Drawing.Point(112, 176);
            this.chkRememberMe.Name = "chkRememberMe";
            this.chkRememberMe.Properties.Appearance.Font = new System.Drawing.Font("Tahoma", 10F);
            this.chkRememberMe.Properties.Appearance.Options.UseFont = true;
            this.chkRememberMe.Properties.Caption = "Remember Me";
            this.chkRememberMe.Size = new System.Drawing.Size(112, 20);
            this.chkRememberMe.TabIndex = 4;
            // 
            // imgCar
            // 
            this.imgCar.Image = global::DVLD_System.Properties.Resources.picCar;
            this.imgCar.ImageRotate = 0F;
            this.imgCar.Location = new System.Drawing.Point(8, 8);
            this.imgCar.Name = "imgCar";
            this.imgCar.Size = new System.Drawing.Size(248, 176);
            this.imgCar.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.imgCar.TabIndex = 0;
            this.imgCar.TabStop = false;
            // 
            // ucLogin
            // 
            this.Controls.Add(this.grpLogin);
            this.Controls.Add(this.pnlLogin);
            this.Name = "ucLogin";
            this.Size = new System.Drawing.Size(702, 460);
            this.pnlLogin.ResumeLayout(false);
            this.pnlLogin.PerformLayout();
            this.grpLogin.ResumeLayout(false);
            this.grpLogin.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.imgVisionClose)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.imgVisionOpen)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.txtUsername.Properties)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chkRememberMe.Properties)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.imgCar)).EndInit();
            this.ResumeLayout(false);

        }



        private void btnClose2_Click(object sender, EventArgs e)
        {
            Application.Exit();
            //this.FindForm().Close();
        }

        private void btnLogin_Click(object sender, EventArgs e)
        {
            this.FindForm().Hide();

            frmMain frm = new frmMain();
            frm.Show();
        }

        private void imgVisionOpen_Click(object sender, EventArgs e)
        {
            txtPassword.UseSystemPasswordChar = true;
            imgVisionOpen.Visible = false;
            imgVisionClose.Visible = true;

        }

        private void imgVisionClose_Click(object sender, EventArgs e)
        {
            txtPassword.UseSystemPasswordChar = false;
            imgVisionOpen.Visible = true;
            imgVisionClose.Visible = false;
        }

        public void FocusUserName()
        {

            txtUsername.Focus();

        }
  

    }
}
