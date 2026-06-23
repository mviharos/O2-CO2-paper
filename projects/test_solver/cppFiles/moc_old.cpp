#include "../../source/first_blood.h"
#include <string>
#include <chrono>
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
   using std::chrono::high_resolution_clock;
   using std::chrono::duration_cast;
   using std::chrono::duration;
   using std::chrono::milliseconds;
   // basic stuff
	//string case_folder = "../../models/test_cases/";
   string case_folder = "../../models/";
   double heart_rate = 75.6;  // if there is a heart model   
   double period_time = 60./heart_rate;
   ofstream fout;
   fout.open("runtimes_moc.txt", ios::app);

   // tested models
   vector<string> case_names;
   case_names.push_back(argv[1]);
   int st = 1; // 0, 1
   string sn = "Moc"; // "MacCormack", "MoC"
   string sf = "results_moc"; // results_maccormack, "results_moc"

   cout << "[O] SOLVER: " << sn << endl;

   for(int i=0; i<case_names.size(); i++)
   {
      cout << " [*] case: " << case_names[i] << endl;
      // loading original case
      first_blood *fb = new first_blood(case_folder + case_names[i]);
      cout << "   + load: OK" << endl;

      //fb->time_end = sim_time;
      fb->time_period = period_time;
      fb->is_periodic_run = false;
      fb->solver_type = st;
      //fb->time_node = "n1";

      fb->material_type = 1; // olufsen model
      vector<double> olufsen_def_const{2.e6,-2253.,8.65e4}; // default constants for olufsen model
      fb->material_const = olufsen_def_const;
    
      // running the simulation
      auto t1 = high_resolution_clock::now();
      bool is_run_ok = fb->run();
      cout << "   + run: OK" << endl;
      auto t2 = high_resolution_clock::now();
      auto ms_int = duration_cast<milliseconds>(t2 - t1);
      fout << std::to_string(ms_int.count()) << endl;

      if(is_run_ok)
      {
         fb->save_results(sf + "/" + case_names[i]);
         cout << "   + save: OK" << endl;
      }
   }
   fout.close();

   return 0;
}
