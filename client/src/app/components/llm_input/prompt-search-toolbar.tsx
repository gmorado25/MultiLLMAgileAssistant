import { FC, useEffect, useState } from "react";
import { Button } from "@mui/joy";
import {
  setPromptSearch,
  useLLMStore,
} from "@/app/zustand-stores/page/store/LLM-store";
import * as yup from "yup";
import _ from "lodash";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import useSearchPrompts from "@/app/zustand-stores/page/hooks/use-search-prompts";

type PromptSearchFormSchema = {
  role?: string;
  phase?: string;
  searchInput?: string;
};

const initialPromptSearchFormValues: PromptSearchFormSchema = {
  role: "",
  phase: "",
  searchInput: "",
};

const PROMPT_SEARCH_FORM_SCHEMA = yup.object().shape({
  role: yup.string(),
  phase: yup.string(),
  searchInput: yup.string(),
});

const PromptSearchToolbar: FC = () => {
  useSearchPrompts();
  
  const [uniqueRoles, setUniqueRoles] = useState<string[]>([]);
  const [uniquePhases, setUniquePhases] = useState<string[]>([]);

  // Capture the initial unique values for role and sdlc_phase
  useEffect(() => {
    const promptData = useLLMStore.use.prompts();
    setUniqueRoles(_.uniq(promptData.map(({ role }) => role)));
    setUniquePhases(_.uniq(promptData.map(({ sdlc_phase }) => sdlc_phase)));
  }, []);

  const { register, handleSubmit } = useForm<PromptSearchFormSchema>({
    mode: "onChange",
    resolver: yupResolver(PROMPT_SEARCH_FORM_SCHEMA),
    defaultValues: { ...initialPromptSearchFormValues },
  });

  const onSearchHandler = async (searchFormValues: PromptSearchFormSchema) => {
    const safeValues = {
      role: searchFormValues.role || "",
      phase: searchFormValues.phase || "",
      searchInput: searchFormValues.searchInput || "",
    };
    setPromptSearch(safeValues);
  };

  return (
    <form
      className="flex justify-between"
      onSubmit={handleSubmit(onSearchHandler)}
    >
      <div className="flex w-1/2 justify-start">
        <div>
          <select className="m-4" placeholder="Role" {...register("role")}>
            <option value="" disabled selected>
              Select Role
            </option>
            <option value="">None</option>
            {_.uniq(uniqueRoles.map((role) => role)).map((role) => (
              <option value={role} key={role}>
                {role}
              </option>
            ))}
          </select>
        </div>
        <div>
          <select className="m-4" placeholder="SDLC" {...register("phase")}>
            <option value="" disabled selected>
              Select SDLC Phase
            </option>
            <option value="">None</option>
            {_.uniq(uniquePhases.map((sdlc_phase) => sdlc_phase)).map(
              (sdlc_phase) => (
                <option value={sdlc_phase} key={sdlc_phase}>
                  {sdlc_phase}
                </option>
              )
            )}
          </select>
        </div>
      </div>
      <div className="flex w-1/2 justify-end">
        <input
          className="m-4"
          placeholder="Search"
          {...register("searchInput")}
        />
        <Button type="submit">Search</Button>
      </div>
    </form>
  );
};

export default PromptSearchToolbar;
