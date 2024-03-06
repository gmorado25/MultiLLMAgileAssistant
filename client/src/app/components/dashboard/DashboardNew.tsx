import Link from "next/link";
import Image from "next/image";
import LlmInputSearchToolbar from "@/app/components/llm_input_new/llm-input-search-toolbar";
import OutputBlock from "@/app/components/llm_output/outputBlock";
import {Footer} from "@/app/components/layouts/footer";
import {useLLMStore} from "@/app/zustand-stores/page/store/LLM-store";
import Button from '@mui/material/Button';
import { createTheme } from '@mui/material/styles';

const theme = createTheme({
    palette: {
        primary: {
            main: '#00579b',
            light: '#4f83cc',
            dark: '#002f6c',
            contrastText: '#ffffff',
        },
    },
});



export const Dashboard = () => {
    const outputData = useLLMStore.use.outputData();
    return (
        <div>
            <LlmInputSearchToolbar></LlmInputSearchToolbar>
            {!!outputData && (
                <div className="Outputs flex flex-row">
                    {outputData.map(({model, response}) => (
                        <OutputBlock
                            key={model}
                            llm={model}
                            output={response}
                        ></OutputBlock>
                    ))}
                </div>
            )}
        </div>
    );
}
