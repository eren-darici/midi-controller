using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace midi_controller_ui
{
    class customProcess : System.Diagnostics.Process
    {
        private static customProcess _instance;
        static int instanceId;

        public void delInstance()
        {
            if (_instance != null)
            {
                this.Kill(true);
                _instance = null;
            }
            
        }

        public static customProcess Instance
        {
            get
            {
                if (_instance == null)
                {
                    _instance = new customProcess();
                }
                return _instance;
            }
        }

        public int getId()
        {
            return instanceId;
        }

        public static customProcess GetCustomProcessById(int id)
        {
            if (id == instanceId)
            {
                return _instance;
            }

            return null;

        }
    }
}
