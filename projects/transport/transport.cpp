#include "../../source/first_blood.h"
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
   // basic stuff
	string case_folder = "../../models/";
   double save_dt = 1e-2;
   //string case_folder = "../../models/";
   double heart_rate = 75.6;  // if there is a heart model

   double period_time = 60./heart_rate;

   // tested models
   vector<string> case_names;

   //case_names.push_back("Bathsheba_CO2_pul_n1");
   //case_names.push_back("Bathsheba_CO2_pul_3");
   //case_names.push_back("Bathsheba_CO2_pul_2");
   //case_names.push_back("Bathsheba_CO2_pul_1");
   case_names.push_back("Bathsheba_CO2_pul_CCC_co2control");
   //case_names.push_back("Bathsheba_CO2_pul");
   //case_names.push_back("Bathsheba_CO2_pul_exercise"); 
   //case_names.push_back("Bathsheba_CO2_pul_mass_con");


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
      //cout<< "alma";cout<< "alma";

      //fb->time_end = sim_time;
      fb->material_type = 1; // setting to olufsen 1, linear 0
      //vector<double> olufsen_def_const{2.e6,-2253.,8.65e4}; // default constants for olufsen model
      //fb->material_const = olufsen_def_const;
      fb->time_period = period_time;
      fb->is_periodic_run = false;
      fb->solver_type = st;


      fb->clear_save_memory();
      //
      string model_name1 = "arterial";
      string model_type1 = "moc";
      vector<string> el{"A1","A12","A16","A6","A20","A55","A8"};
      vector<string> nl{};
      fb->set_save_memory(model_name1,model_type1,el,nl);

      string model_name12 = "heart_kim_lit";
      string model_type12 = "lumped";
      vector<string> e12{"C_pa"};
      vector<string> n12{"p_RV2"};
      for(int k=0;k<fb->lum.size();k++)
         {
            if(fb->lum[k]->name == "heart_kim_lit")
               {
                  fb->lum[k]->set_save_memory(e12, n12);
               }
         }


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

      //string model_name8 = "venous";
      //string model_type8 = "moc";
      //vector<string> e2{"189","215","84"};
      //vector<string> n2{};
      //fb->set_save_memory(model_name8,model_type8,e2,n2);

      string model_name10 = "heart_kim_lit";
      string model_type10 = "CO2_transport++";
      fb->set_save_memory(model_name10,model_type10,e3,n3);


      vector<string> e20{"R1","R2","R3"};
      vector<string> n20{"Q1"};
      //saving a lot of peripheral stuff for reference autiregualtion
      for (int k = 0; k < fb->lum.size(); k++) {
         for(int j = 4; j< 47; j++){
            if (fb->lum[k]->name == "p" + std::to_string(j)) {
              fb->set_save_memory("p" + std::to_string(j),"CO2_transport++",e3,n3);
              fb->set_save_memory("p" + std::to_string(j),"lumped",e20,n20);
          }
       }
      }


    
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
         //fb->save_results(case_names[i],model_name8 ,model_type8 ,e2,n2);
         //fb->save_results(case_names[i],model_name9 ,model_type9,el,nl );
         fb->save_results(case_names[i],model_name9 ,model_type9 ,e3,n3);
         fb->save_results(case_names[i],model_name10 ,model_type10 ,e3,n3);

         //fb->save_results(case_names[i],model_name12 ,model_type12 ,e12,n12);

         //o2 and co2 concentrations in the capillaries
         
/*
         for(int i=0;i<fb->lum.size();i++){
            if(fb->lum[i]->name == "heart_kim_lit"){
               fb->lum[i]->saveVectorToFile(fb->lum[i]->pul_cap_CO2_pla->fi, "results//" +case_names[i]+ "//heart_kim_lit//co2_pla_x.txt");
               fb->lum[i]->saveVectorToFile(fb->lum[i]->pul_cap_PO2->fi, "results//" +case_names[i]+ "//heart_kim_lit//o2_pla_x.txt");}

            if(fb->lum[i]->name == "p10"){
               fb->lum[i]->saveVectorToFile(fb->lum[i]->per_cap_CO2_pla->fi, "results//" +case_names[i]+ "//p10//co2_pla_x.txt");
               fb->lum[i]->saveVectorToFile(fb->lum[i]->per_cap_PO2->fi, "results//" +case_names[i]+ "//p10//o2_pla_x.txt");}
         }*/

         //for(int i=0;i<fb->lum.size();i++){if(fb->lum[i]->name == "heart_kim_lit"){ fb->lum[i]->save_results( 0.001, case_names[i], e12, n12);   }}
         //for(int i=0;i<fb->lum.size();i++){if(fb->lum[i]->name == "heart_kim_lit"){ fb->lum[i]->save_results(case_names[i], e12, n12);}}

         /*for(int i=0;i<fb->lum.size();i++){
            if(fb->lum[i]->name == "heart_kim_lit"){ 
               for (int j =0; j <fb->lum[i]->edges.size(); j++ ){
                  if (fb->lum[i]->edges[j]->name == "C_pa"){fb->lum[i]->saveVectorToFile(fb->lum[i]->edges[j]->volume_flow_rate, "results//Bathsheba_CO2_pul//heart_kim_lit//C_pa.txt");}

                  if (fb->lum[i]->nodes[j]->name == "p_RV2"){fb->lum[i]->saveVectorToFile(fb->lum[i]->nodes[j]->pressure, "results//Bathsheba_CO2_pul//heart_kim_lit//p_RV2.txt");}
               }*/
            

            //fb->lum[i]->saveVectorToFile(fb->lum[i]->per_cap_PO2->fi, "results//Bathsheba_CO2_pul//heart_kim_lit//C_pa.txt");
            //fb->lum[i]->saveVectorToFile(fb->lum[i]->per_cap_PO2->fi, "results//Bathsheba_CO2_pul//heart_kim_lit//p_RV2.txt");}}





         for (int k = 0; k < fb->lum.size(); k++) {
            for(int j = 4; j< 48; j++){
               if (fb->lum[k]->name == "p" + std::to_string(j)) {
                  fb->save_results(case_names[i],"p" + std::to_string(j),"CO2_transport++",e3,n3);
                  fb->lum[k]->saveVectorsToFile(fb->lum[k]-> time, fb->lum[k]->nodes[5]->pressure, "results//" +case_names[i]+ "//p"+ std::to_string(j) +"//Q1.txt");
                  fb->lum[k]->saveVectorsToFile(fb->lum[k]-> time, fb->lum[k]->edges[1]->volume_flow_rate, "results//" +case_names[i]+ "//p"+ std::to_string(j) +"//R1.txt");
                  fb->lum[k]->saveVectorsToFile(fb->lum[k]-> time, fb->lum[k]->edges[2]->volume_flow_rate, "results//" +case_names[i]+ "//p"+ std::to_string(j) +"//R2.txt");
                  fb->lum[k]->saveVectorsToFile(fb->lum[k]-> time, fb->lum[k]->edges[3]->volume_flow_rate, "results//" +case_names[i]+ "//p"+ std::to_string(j) +"//R3.txt");
                  fb->lum[k]->save_tissueO2("results//"+ case_names[i] +"//p" + std::to_string(j) + "//tissueO2.txt", fb->lum[k]-> time);
            }
            
         }
         }


            //}
         //}
      //}

/*
      fb->clear_save_memory();
      string model_name = "arterial";
      string model_type = "moc";
      vector<string> el{"A1","A12","A55","A8","A79"};
      vector<string> nl{"p33","p35"};
      fb->set_save_memory(model_name,model_type,el,nl);
    
      // running the simulation
      bool is_run_ok = fb->run();
      cout << "   + run: OK" << endl;

      if(is_run_ok)
      {
         //fb->save_results(sf + "/" + case_names[i]);
         //fb->save_results();
         //cout << "   + save: OK" << endl;
         fb->save_results(case_names[i],model_name,model_type,el,nl);
      }*/



      }

   }

   return 0;
}
