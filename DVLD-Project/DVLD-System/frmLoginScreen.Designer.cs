namespace DVLD_System
{
    partial class frmLoginScreen
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmLoginScreen));
            this.ucLogin1 = new DVLD_System.ucLogin();
            this.SuspendLayout();
            // 
            // ucLogin1
            // 
            this.ucLogin1.Location = new System.Drawing.Point(32, 0);
            this.ucLogin1.Name = "ucLogin1";
            this.ucLogin1.Size = new System.Drawing.Size(702, 460);
            this.ucLogin1.TabIndex = 0;
            // 
            // frmLoginScreen
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(760, 471);
            this.Controls.Add(this.ucLogin1);
            this.IconOptions.Image = ((System.Drawing.Image)(resources.GetObject("frmLoginScreen.IconOptions.Image")));
            this.Name = "frmLoginScreen";
            this.Text = "XtraForm1";
            this.Shown += new System.EventHandler(this.frmLoginScreen_Shown);
            this.ResumeLayout(false);

        }

        #endregion

        private ucLogin ucLogin1;
    }
}