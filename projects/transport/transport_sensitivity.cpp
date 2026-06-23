#include "../../source/first_blood.h"
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
   // basic stuff
	string case_folder = "../../models/";
   double save_dt = 1e-2;
   double heart_rate = 75.6;  // if there is a heart model

   double period_time = 60./heart_rate;

   // tested models
   vector<string> case_names;

   int n_par = 22;

   if (argc != n_par) {
    cout << "\n\nwrong number of inputs!!!!!!!!!!!!!!\n";
    return 1;   // <<< REQUIRED
   }

   //scaling factors
   double fi_cap_mul = stod(argv[1],0);
   double fi_rbc_mul = stod(argv[2],0);
   double ksi_c_mul = stod(argv[3],0);
   double ksi_pla_mul = stod(argv[4],0);
   double alpha_o2_tis_mul = stod(argv[5],0);
   double alpha_o2_blo_mul = stod(argv[6],0);
   double alpha_co2_pla_mul = stod(argv[7],0);
   double alpha_co2_rbc_mul = stod(argv[8],0);
   double beta_hco3_rbc_mul = stod(argv[9],0);
   double beta_hco3_pla_mul = stod(argv[10],0);
   double RQ_mul = stod(argv[11],0);
   double Mmax_mul = stod(argv[12],0);
   double C_O2_50_mul = stod(argv[13],0);
   double kappa_O2_cap_mul = stod(argv[14],0);
   double Sc_Vc_mul = stod(argv[15],0);
   double hcap_mul = stod(argv[16],0);
   double tao_pla_rbc_mul = stod(argv[17],0);
   double tao_hco3pla_rbc_mul = stod(argv[18],0);
   double tao_O2_mul = stod(argv[19],0);
   double tao_HbCO2_mul = stod(argv[20],0);
   double tao_HCO3_mul = stod(argv[21],0);



   case_names.push_back("Bathsheba_CO2_pul");



   int st = 0; // 0 ="MacCormack", 1 = "MoC"
   string sn = "0D"; // "MacCormack", "MoC"
   string sf = "results"; // results_maccormack, "results_moc"

   cout << "[O] SOLVER: " << sn << endl;

   for(int i=0; i<case_names.size(); i++)
   {
      cout << " [*] case: " << case_names[i] << endl;
      // loading original case
      first_blood *fb = new first_blood(case_folder + case_names[i]);
      cout << "   + load: OK" << endl;


      // setting parameters
      for(int i=0;i<fb->lum.size();i++){
         fb->lum[i]->fi_c     *= fi_cap_mul;
         fb->lum[i]->fi_rbc   *= fi_rbc_mul;
         fb->lum[i]->ksi_c    *= ksi_c_mul;
         fb->lum[i]->ksi_pla  *= ksi_pla_mul;

         fb->lum[i]->alpha_t  *= alpha_o2_tis_mul;
         fb->lum[i]->alpha_b  *= alpha_o2_blo_mul;
         fb->lum[i]->alpha_co2_pla     *= alpha_co2_pla_mul;
         fb->lum[i]->alpha_co2_rbc     *= alpha_co2_rbc_mul;

         fb->lum[i]->alpha_hco3_rbc     *= beta_hco3_rbc_mul;
         fb->lum[i]->alpha_hco3_pla     *= beta_hco3_pla_mul;
         fb->lum[i]->RQ     *= RQ_mul;
         fb->lum[i]->Mmax *= Mmax_mul;

         fb->lum[i]->C50 *= C_O2_50_mul;
         fb->lum[i]->kc *= kappa_O2_cap_mul;
         fb->lum[i]->S_V_c *= Sc_Vc_mul;
         fb->lum[i]->hc *= hcap_mul;

         fb->lum[i]->tao_co2_pla_rbc *= tao_pla_rbc_mul;
         fb->lum[i]->tao_hco3_pla_rbc *= tao_hco3pla_rbc_mul;

         fb->lum[i]->taoO2 *= tao_O2_mul;
         fb->lum[i]->taoO2_p *= tao_O2_mul;

         fb->lum[i]->tao_hbco2 *= tao_HbCO2_mul;
         fb->lum[i]->tao_hco3 *= tao_HCO3_mul;


         //other parameters changing
         fb->lum[i]->fi_t = 1-fb->lum[i]->fi_c;
         fb->lum[i]->fi_pla = 1-fb->lum[i]->fi_rbc;
         fb->lum[i]->tao_co2_rbc_pla = fb->lum[i]->fi_rbc/fb->lum[i]->fi_pla*fb->lum[i]->alpha_co2_rbc/fb->lum[i]->alpha_co2_pla*fb->lum[i]->tao_co2_pla_rbc;
         fb->lum[i]->tao_hco3_rbc_pla = fb->lum[i]->fi_rbc/fb->lum[i]->fi_pla*fb->lum[i]->alpha_hco3_rbc/fb->lum[i]->alpha_hco3_pla*fb->lum[i]->tao_hco3_pla_rbc;
      }





      //fb->time_end = sim_time;
      fb->material_type = 1; // setting to olufsen 1, linear 0


      fb->time_period = period_time;
      fb->is_periodic_run = false;
      fb->solver_type = st;
      //fb->time_node = "n1";



      fb->clear_save_memory();
      //
      string model_name1 = "arterial";
      string model_type1 = "moc";
      vector<string> el{"A1","A12","A55","A8"};
      vector<string> nl{};
      fb->set_save_memory(model_name1,model_type1,el,nl);


      //for transport
      //string model_name2 = "p10";
      //string model_type2 = "RBC_transport";
      //fb->set_save_memory(model_name2,model_type2,el,nl);

      //string model_name3 = "heart_kim_lit";
      //string model_type3 = "RBC_transport";
      //fb->set_save_memory(model_name3,model_type3,el,nl);

      string model_name4 = "p10";
      string model_type4 = "HBsat_transport";
      fb->set_save_memory(model_name4,model_type4,el,nl);

      string model_name5 = "heart_kim_lit";
      string model_type5 = "HBsat_transport";
      fb->set_save_memory(model_name5,model_type5,el,nl);

      string model_name6 = "p10";
      string model_type6 = "PlasmaO2_transport";
      fb->set_save_memory(model_name6,model_type6,el,nl);

      string model_name7 = "heart_kim_lit";
      string model_type7 = "PlasmaO2_transport";
      fb->set_save_memory(model_name7,model_type7,el,nl);


      //CO2 transport
      vector<string> e3{};
      vector<string> n3{};
      string model_name9 = "p10";
      string model_type9 = "CO2_transport++";
      fb->set_save_memory(model_name9,model_type9,e3,n3);

      string model_name8 = "venous";
      string model_type8 = "moc";
      vector<string> e2{"189","215","84"};
      vector<string> n2{};
      fb->set_save_memory(model_name8,model_type8,e2,n2);

      string model_name10 = "heart_kim_lit";
      string model_type10 = "CO2_transport++";
      fb->set_save_memory(model_name10,model_type10,e2,n2);
    
      // running the simulation
      
      bool is_run_ok = fb->run();
      cout << "   + run: OK" << endl;

      if(is_run_ok)
      {
         //fb->save_results(sf + "/" + case_names[i]);
         //fb->save_results(save_dt);
         //cout << "   + save: OK" << endl;
         fb->save_results(case_names[i],model_name1 ,model_type1 ,el,nl);
         //fb->save_results();
         //fb->save_results(case_names[i],model_name2 ,model_type2 ,el,nl);
         //fb->save_results(case_names[i],model_name3 ,model_type3 ,el,nl);
         fb->save_results(case_names[i],model_name4 ,model_type4 ,el,nl);
         fb->save_results(case_names[i],model_name5 ,model_type5 ,el,nl);
         fb->save_results(case_names[i],model_name6 ,model_type6 ,el,nl);
         fb->save_results(case_names[i],model_name7 ,model_type7 ,el,nl);
         fb->save_results(case_names[i],model_name8 ,model_type8 ,e2,n2);
         //fb->save_results(case_names[i],model_name9 ,model_type9,el,nl );
         fb->save_results(case_names[i],model_name9 ,model_type9 ,e3,n3);
         fb->save_results(case_names[i],model_name10 ,model_type10 ,e3,n3);


      }


   }

   return 0;
}
