import enum
from kagglesdk.kaggle_object import *
from typing import List, Optional

class ToolProvider(enum.Enum):
  """Tool providers available to the content discovery agent."""
  TOOL_PROVIDER_UNSPECIFIED = 0
  TOOL_PROVIDER_KAGGLE = 1
  """Kaggle MCP tools"""
  TOOL_PROVIDER_ARXIV = 2
  """arXiv academic paper search."""
  TOOL_PROVIDER_KAGGLE_RESEARCH = 3
  """Kaggle research sub-agent"""
  TOOL_PROVIDER_WEB_RESEARCH = 4
  """Web research via Gemini grounding (Google Search + URL fetch)."""

class AgentRunStats(KaggleObject):
  r"""
  Attributes:
    total_turns (int)
    total_tool_calls (int)
    cumulative_input_tokens (int)
      Sum of each turn's input tokens (for cost tracking).
    cumulative_output_tokens (int)
      Sum of each turn's output tokens (for cost tracking).
    final_context_tokens (int)
      Last turn's prompt tokens (context window usage).
    model_name (str)
  """

  def __init__(self):
    self._total_turns = 0
    self._total_tool_calls = 0
    self._cumulative_input_tokens = 0
    self._cumulative_output_tokens = 0
    self._final_context_tokens = 0
    self._model_name = ""
    self._freeze()

  @property
  def total_turns(self) -> int:
    return self._total_turns

  @total_turns.setter
  def total_turns(self, total_turns: int):
    if total_turns is None:
      del self.total_turns
      return
    if not isinstance(total_turns, int):
      raise TypeError('total_turns must be of type int')
    self._total_turns = total_turns

  @property
  def total_tool_calls(self) -> int:
    return self._total_tool_calls

  @total_tool_calls.setter
  def total_tool_calls(self, total_tool_calls: int):
    if total_tool_calls is None:
      del self.total_tool_calls
      return
    if not isinstance(total_tool_calls, int):
      raise TypeError('total_tool_calls must be of type int')
    self._total_tool_calls = total_tool_calls

  @property
  def cumulative_input_tokens(self) -> int:
    """Sum of each turn's input tokens (for cost tracking)."""
    return self._cumulative_input_tokens

  @cumulative_input_tokens.setter
  def cumulative_input_tokens(self, cumulative_input_tokens: int):
    if cumulative_input_tokens is None:
      del self.cumulative_input_tokens
      return
    if not isinstance(cumulative_input_tokens, int):
      raise TypeError('cumulative_input_tokens must be of type int')
    self._cumulative_input_tokens = cumulative_input_tokens

  @property
  def cumulative_output_tokens(self) -> int:
    """Sum of each turn's output tokens (for cost tracking)."""
    return self._cumulative_output_tokens

  @cumulative_output_tokens.setter
  def cumulative_output_tokens(self, cumulative_output_tokens: int):
    if cumulative_output_tokens is None:
      del self.cumulative_output_tokens
      return
    if not isinstance(cumulative_output_tokens, int):
      raise TypeError('cumulative_output_tokens must be of type int')
    self._cumulative_output_tokens = cumulative_output_tokens

  @property
  def final_context_tokens(self) -> int:
    """Last turn's prompt tokens (context window usage)."""
    return self._final_context_tokens

  @final_context_tokens.setter
  def final_context_tokens(self, final_context_tokens: int):
    if final_context_tokens is None:
      del self.final_context_tokens
      return
    if not isinstance(final_context_tokens, int):
      raise TypeError('final_context_tokens must be of type int')
    self._final_context_tokens = final_context_tokens

  @property
  def model_name(self) -> str:
    return self._model_name

  @model_name.setter
  def model_name(self, model_name: str):
    if model_name is None:
      del self.model_name
      return
    if not isinstance(model_name, str):
      raise TypeError('model_name must be of type str')
    self._model_name = model_name


class AgentToolCall(KaggleObject):
  r"""
  Attributes:
    tool_name (str)
    arguments_json (str)
    result_summary (str)
  """

  def __init__(self):
    self._tool_name = ""
    self._arguments_json = ""
    self._result_summary = ""
    self._freeze()

  @property
  def tool_name(self) -> str:
    return self._tool_name

  @tool_name.setter
  def tool_name(self, tool_name: str):
    if tool_name is None:
      del self.tool_name
      return
    if not isinstance(tool_name, str):
      raise TypeError('tool_name must be of type str')
    self._tool_name = tool_name

  @property
  def arguments_json(self) -> str:
    return self._arguments_json

  @arguments_json.setter
  def arguments_json(self, arguments_json: str):
    if arguments_json is None:
      del self.arguments_json
      return
    if not isinstance(arguments_json, str):
      raise TypeError('arguments_json must be of type str')
    self._arguments_json = arguments_json

  @property
  def result_summary(self) -> str:
    return self._result_summary

  @result_summary.setter
  def result_summary(self, result_summary: str):
    if result_summary is None:
      del self.result_summary
      return
    if not isinstance(result_summary, str):
      raise TypeError('result_summary must be of type str')
    self._result_summary = result_summary


class AgentTurnDetail(KaggleObject):
  r"""
  Attributes:
    turn_number (int)
    prompt_token_count (int)
      Context window size at this turn.
    candidates_token_count (int)
      Model output tokens for this turn.
    tool_calls (AgentToolCall)
    duration_ms (int)
      Wall-clock time for this turn in milliseconds.
  """

  def __init__(self):
    self._turn_number = 0
    self._prompt_token_count = 0
    self._candidates_token_count = 0
    self._tool_calls = []
    self._duration_ms = 0
    self._freeze()

  @property
  def turn_number(self) -> int:
    return self._turn_number

  @turn_number.setter
  def turn_number(self, turn_number: int):
    if turn_number is None:
      del self.turn_number
      return
    if not isinstance(turn_number, int):
      raise TypeError('turn_number must be of type int')
    self._turn_number = turn_number

  @property
  def prompt_token_count(self) -> int:
    """Context window size at this turn."""
    return self._prompt_token_count

  @prompt_token_count.setter
  def prompt_token_count(self, prompt_token_count: int):
    if prompt_token_count is None:
      del self.prompt_token_count
      return
    if not isinstance(prompt_token_count, int):
      raise TypeError('prompt_token_count must be of type int')
    self._prompt_token_count = prompt_token_count

  @property
  def candidates_token_count(self) -> int:
    """Model output tokens for this turn."""
    return self._candidates_token_count

  @candidates_token_count.setter
  def candidates_token_count(self, candidates_token_count: int):
    if candidates_token_count is None:
      del self.candidates_token_count
      return
    if not isinstance(candidates_token_count, int):
      raise TypeError('candidates_token_count must be of type int')
    self._candidates_token_count = candidates_token_count

  @property
  def tool_calls(self) -> Optional[List[Optional['AgentToolCall']]]:
    return self._tool_calls

  @tool_calls.setter
  def tool_calls(self, tool_calls: Optional[List[Optional['AgentToolCall']]]):
    if tool_calls is None:
      del self.tool_calls
      return
    if not isinstance(tool_calls, list):
      raise TypeError('tool_calls must be of type list')
    if not all([isinstance(t, AgentToolCall) for t in tool_calls]):
      raise TypeError('tool_calls must contain only items of type AgentToolCall')
    self._tool_calls = tool_calls

  @property
  def duration_ms(self) -> int:
    """Wall-clock time for this turn in milliseconds."""
    return self._duration_ms

  @duration_ms.setter
  def duration_ms(self, duration_ms: int):
    if duration_ms is None:
      del self.duration_ms
      return
    if not isinstance(duration_ms, int):
      raise TypeError('duration_ms must be of type int')
    self._duration_ms = duration_ms


class RunContentDiscoveryAgentRequest(KaggleObject):
  r"""
  Attributes:
    query (str)
      Required prompt for the agent.
    max_agent_turns (int)
      Maximum number of agent turns.
    include_turn_details (bool)
      When true, response includes per-turn breakdown.
    model_name (str)
      Overrides the default model (e.g. 'gemini-2.5-pro').
    system_prompt (str)
      Overrides the default system prompt.
    disabled_providers (ToolProvider)
      Tool providers to disable. Providers not listed here remain enabled.
  """

  def __init__(self):
    self._query = ""
    self._max_agent_turns = 0
    self._include_turn_details = False
    self._model_name = ""
    self._system_prompt = ""
    self._disabled_providers = []
    self._freeze()

  @property
  def query(self) -> str:
    """Required prompt for the agent."""
    return self._query

  @query.setter
  def query(self, query: str):
    if query is None:
      del self.query
      return
    if not isinstance(query, str):
      raise TypeError('query must be of type str')
    self._query = query

  @property
  def max_agent_turns(self) -> int:
    """Maximum number of agent turns."""
    return self._max_agent_turns

  @max_agent_turns.setter
  def max_agent_turns(self, max_agent_turns: int):
    if max_agent_turns is None:
      del self.max_agent_turns
      return
    if not isinstance(max_agent_turns, int):
      raise TypeError('max_agent_turns must be of type int')
    self._max_agent_turns = max_agent_turns

  @property
  def include_turn_details(self) -> bool:
    """When true, response includes per-turn breakdown."""
    return self._include_turn_details

  @include_turn_details.setter
  def include_turn_details(self, include_turn_details: bool):
    if include_turn_details is None:
      del self.include_turn_details
      return
    if not isinstance(include_turn_details, bool):
      raise TypeError('include_turn_details must be of type bool')
    self._include_turn_details = include_turn_details

  @property
  def model_name(self) -> str:
    """Overrides the default model (e.g. 'gemini-2.5-pro')."""
    return self._model_name

  @model_name.setter
  def model_name(self, model_name: str):
    if model_name is None:
      del self.model_name
      return
    if not isinstance(model_name, str):
      raise TypeError('model_name must be of type str')
    self._model_name = model_name

  @property
  def system_prompt(self) -> str:
    """Overrides the default system prompt."""
    return self._system_prompt

  @system_prompt.setter
  def system_prompt(self, system_prompt: str):
    if system_prompt is None:
      del self.system_prompt
      return
    if not isinstance(system_prompt, str):
      raise TypeError('system_prompt must be of type str')
    self._system_prompt = system_prompt

  @property
  def disabled_providers(self) -> Optional[List['ToolProvider']]:
    """Tool providers to disable. Providers not listed here remain enabled."""
    return self._disabled_providers

  @disabled_providers.setter
  def disabled_providers(self, disabled_providers: Optional[List['ToolProvider']]):
    if disabled_providers is None:
      del self.disabled_providers
      return
    if not isinstance(disabled_providers, list):
      raise TypeError('disabled_providers must be of type list')
    if not all([isinstance(t, ToolProvider) for t in disabled_providers]):
      raise TypeError('disabled_providers must contain only items of type ToolProvider')
    self._disabled_providers = disabled_providers


class RunContentDiscoveryAgentResponse(KaggleObject):
  r"""
  Attributes:
    markdown_output (str)
      Markdown-formatted output from the agent.
    stats (AgentRunStats)
      Run-level statistics (token usage, turns, etc.).
    turn_details (AgentTurnDetail)
      Per-turn breakdown. Only populated when include_turn_details is set.
  """

  def __init__(self):
    self._markdown_output = ""
    self._stats = None
    self._turn_details = []
    self._freeze()

  @property
  def markdown_output(self) -> str:
    """Markdown-formatted output from the agent."""
    return self._markdown_output

  @markdown_output.setter
  def markdown_output(self, markdown_output: str):
    if markdown_output is None:
      del self.markdown_output
      return
    if not isinstance(markdown_output, str):
      raise TypeError('markdown_output must be of type str')
    self._markdown_output = markdown_output

  @property
  def stats(self) -> Optional['AgentRunStats']:
    """Run-level statistics (token usage, turns, etc.)."""
    return self._stats

  @stats.setter
  def stats(self, stats: Optional['AgentRunStats']):
    if stats is None:
      del self.stats
      return
    if not isinstance(stats, AgentRunStats):
      raise TypeError('stats must be of type AgentRunStats')
    self._stats = stats

  @property
  def turn_details(self) -> Optional[List[Optional['AgentTurnDetail']]]:
    """Per-turn breakdown. Only populated when include_turn_details is set."""
    return self._turn_details

  @turn_details.setter
  def turn_details(self, turn_details: Optional[List[Optional['AgentTurnDetail']]]):
    if turn_details is None:
      del self.turn_details
      return
    if not isinstance(turn_details, list):
      raise TypeError('turn_details must be of type list')
    if not all([isinstance(t, AgentTurnDetail) for t in turn_details]):
      raise TypeError('turn_details must contain only items of type AgentTurnDetail')
    self._turn_details = turn_details


AgentRunStats._fields = [
  FieldMetadata("totalTurns", "total_turns", "_total_turns", int, 0, PredefinedSerializer()),
  FieldMetadata("totalToolCalls", "total_tool_calls", "_total_tool_calls", int, 0, PredefinedSerializer()),
  FieldMetadata("cumulativeInputTokens", "cumulative_input_tokens", "_cumulative_input_tokens", int, 0, PredefinedSerializer()),
  FieldMetadata("cumulativeOutputTokens", "cumulative_output_tokens", "_cumulative_output_tokens", int, 0, PredefinedSerializer()),
  FieldMetadata("finalContextTokens", "final_context_tokens", "_final_context_tokens", int, 0, PredefinedSerializer()),
  FieldMetadata("modelName", "model_name", "_model_name", str, "", PredefinedSerializer()),
]

AgentToolCall._fields = [
  FieldMetadata("toolName", "tool_name", "_tool_name", str, "", PredefinedSerializer()),
  FieldMetadata("argumentsJson", "arguments_json", "_arguments_json", str, "", PredefinedSerializer()),
  FieldMetadata("resultSummary", "result_summary", "_result_summary", str, "", PredefinedSerializer()),
]

AgentTurnDetail._fields = [
  FieldMetadata("turnNumber", "turn_number", "_turn_number", int, 0, PredefinedSerializer()),
  FieldMetadata("promptTokenCount", "prompt_token_count", "_prompt_token_count", int, 0, PredefinedSerializer()),
  FieldMetadata("candidatesTokenCount", "candidates_token_count", "_candidates_token_count", int, 0, PredefinedSerializer()),
  FieldMetadata("toolCalls", "tool_calls", "_tool_calls", AgentToolCall, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("durationMs", "duration_ms", "_duration_ms", int, 0, PredefinedSerializer()),
]

RunContentDiscoveryAgentRequest._fields = [
  FieldMetadata("query", "query", "_query", str, "", PredefinedSerializer()),
  FieldMetadata("maxAgentTurns", "max_agent_turns", "_max_agent_turns", int, 0, PredefinedSerializer()),
  FieldMetadata("includeTurnDetails", "include_turn_details", "_include_turn_details", bool, False, PredefinedSerializer()),
  FieldMetadata("modelName", "model_name", "_model_name", str, "", PredefinedSerializer()),
  FieldMetadata("systemPrompt", "system_prompt", "_system_prompt", str, "", PredefinedSerializer()),
  FieldMetadata("disabledProviders", "disabled_providers", "_disabled_providers", ToolProvider, [], ListSerializer(EnumSerializer())),
]

RunContentDiscoveryAgentResponse._fields = [
  FieldMetadata("markdownOutput", "markdown_output", "_markdown_output", str, "", PredefinedSerializer()),
  FieldMetadata("stats", "stats", "_stats", AgentRunStats, None, KaggleObjectSerializer()),
  FieldMetadata("turnDetails", "turn_details", "_turn_details", AgentTurnDetail, [], ListSerializer(KaggleObjectSerializer())),
]

